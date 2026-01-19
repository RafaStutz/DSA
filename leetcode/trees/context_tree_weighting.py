from dataclasses import dataclass, field
import math 


@dataclass
class ContextTreeNode:
    """
    A node in a context tree.

    Each node represents a context (a suffix of the past). Is stores:
    - children: mapping from a context symbol -> child node
    - symbol_counts: counts of next-symbol occurrences seen under this context
    - total_count: total number of next-symbol occurrences seen under this context
    """
    alphabet_size: int
    parent: "ContextTreeNode | None" = None
    children: dict[int, "ContextTreeNode"] = field(default_factory=dict)
    symbol_counts: list[int] = field(init=False)
    total_count: int = 0

    log_kt_evidence: float = 0.0
    log_weighted_evidence: float = 0.0


    def __post_init__(self) -> None:
        self.symbol_counts = [0] * self.alphabet_size

    def increment_count_for_symbol(self, symbol: int) -> None:
        self.symbol_counts[symbol] += 1
        self.total_count += 1

        
class ContextTree:
    """
    Context Tree with CTW weighting (incremental, on-demand tree).

    Conventions:
    - Symbols are integers in [0, alphabet_size - 1].
    - A context is a list of past symbols ordered as:
        [most_recent, ..., oldest]
    - We update along the path for context lengths 0..Lmax (root included).

    CTW notes:
    - Local model is KT (Dirichlet-1/2).
    - Weighted evidence mixes local KT evidence and children weighted evidence:
        P_w = 0.5 * P_KT + 0.5 * Π_child P_w(child)
      (implemented in log-space with log-sum-exp)
    - Since the tree is created on-demand, missing children are treated as having
      neutral contribution (P_w = 1, log P_w = 0) in Π_child.
    """

    def __init__(self, maximum_depth: int, alphabet_size: int) -> None:
        if maximum_depth < 0:
            raise ValueError("maximum_depth must be non-negative.")
        if alphabet_size <= 0:
            raise ValueError("alphabet_size must be positive.")
        self.maximum_depth = maximum_depth
        self.alphabet_size = alphabet_size

        
        self.root_node = ContextTreeNode(alphabet_size=self.alphabet_size, parent=None)


    @staticmethod
    def _logsumexp_two(log_a: float, log_b: float) -> float:
        """Compute log(exp(log_a) + exp(log_b)) stably."""
        if log_a == -math.inf:
            return log_b
        if log_b == -math.inf:
            return log_a
        maximum = log_a if log_a >= log_b else log_b
        return maximum + math.log(math.exp(log_a - maximum) + math.exp(log_b - maximum))

    def _update_log_kt_evidence_for_symbol(self, node: ContextTreeNode, observed_symbol: int) -> None:
        """
        Incrementally update log P_KT(data) for this node when a new symbol is observed.

        KT predictive:
            p_KT(x) = (n_x + 1/2) / (N + M/2)
        where n_x and N are counts BEFORE adding the symbol.
        """
        previous_count_for_symbol = node.symbol_counts[observed_symbol]
        previous_total_count = node.total_count

        numerator = previous_count_for_symbol + 0.5
        denominator = previous_total_count + 0.5 * self.alphabet_size

        node.log_kt_evidence += math.log(numerator) - math.log(denominator)

    def _log_children_weighted_product(self, node: ContextTreeNode) -> float:
        """
        Compute log( Π_child P_w(child) ).

        For on-demand trees: missing children are treated as P_w=1 (log=0),
        so we only sum over existing children.
        """
        log_product = 0.0
        for child_node in node.children.values():
            log_product += child_node.log_weighted_evidence
        return log_product

    def _recompute_log_weighted_evidence(self, node: ContextTreeNode) -> None:
        """
        Recompute log P_w(data) at this node using:
            P_w = 0.5 * P_KT + 0.5 * Π_child P_w(child)
        """
        log_half = -math.log(2.0)

        log_kt_term = log_half + node.log_kt_evidence
        log_children_term = log_half + self._log_children_weighted_product(node)

        node.log_weighted_evidence = self._logsumexp_two(log_kt_term, log_children_term)


    def get_nodes_on_context_path(self, past_context: list[int] | tuple[int, ...]) -> list[ContextTreeNode]:
        """
        Return the list of nodes [root, node(ctx[:1]), node(ctx[:2]), ...] up to max depth,
        creating nodes if needed.
        """
        maximum_context_length = min(self.maximum_depth, len(past_context))

        nodes_on_path: list[ContextTreeNode] = [self.root_node]
        current_node = self.root_node

        for context_length in range(1, maximum_context_length + 1):
            context_symbol = past_context[context_length - 1]
            if not (0 <= context_symbol < self.alphabet_size):
                raise ValueError(
                    f"Context symbol {context_symbol} out of range [0, {self.alphabet_size})."
                )

            if context_symbol not in current_node.children:
                current_node.children[context_symbol] = ContextTreeNode(
                    alphabet_size=self.alphabet_size,
                    parent=current_node,
                )
            current_node = current_node.children[context_symbol]
            nodes_on_path.append(current_node)

        return nodes_on_path


    def update(self, observed_symbol: int, past_context: list[int] | tuple[int, ...]) -> None:
        if not (0 <= observed_symbol < self.alphabet_size):
            raise ValueError(f"Observed symbol {observed_symbol} out of range [0, {self.alphabet_size}).")

        nodes_on_path = self.get_nodes_on_context_path(list(past_context))

        # Update local KT evidence and counts at each node on the path
        for node in nodes_on_path:
            self._update_log_kt_evidence_for_symbol(node, observed_symbol)
            node.increment_count_for_symbol(observed_symbol)

        # Recompute weighted evidence bottom-up (deepest -> root)
        for node in reversed(nodes_on_path):
            self._recompute_log_weighted_evidence(node)


    def predict(self, past_context: list[int] | tuple[int, ...]) -> list[float]:
        nodes_on_path = self.get_nodes_on_context_path(list(past_context))

        current_log_pw = self.root_node.log_weighted_evidence
        if current_log_pw == -math.inf:
            # no data; return uniform
            return [1.0 / self.alphabet_size] * self.alphabet_size

        candidate_log_probs: list[float] = []

        for candidate_symbol in range(self.alphabet_size):
            new_log_weighted_evidence_by_node_id: dict[int, float] = {}

            for node in reversed(nodes_on_path):
                previous_count_for_symbol = node.symbol_counts[candidate_symbol]
                previous_total_count = node.total_count
                numerator = previous_count_for_symbol + 0.5
                denominator = previous_total_count + 0.5 * self.alphabet_size
                new_log_kt = node.log_kt_evidence + (math.log(numerator) - math.log(denominator))

                log_children_product = 0.0
                for child_symbol, child_node in node.children.items():
                    child_log_pw = child_node.log_weighted_evidence
                    child_id = id(child_node)
                    if child_id in new_log_weighted_evidence_by_node_id:
                        child_log_pw = new_log_weighted_evidence_by_node_id[child_id]
                    log_children_product += child_log_pw

                log_half = -math.log(2.0)
                log_kt_term = log_half + new_log_kt
                log_children_term = log_half + log_children_product
                new_log_pw = self._logsumexp_two(log_kt_term, log_children_term)

                new_log_weighted_evidence_by_node_id[id(node)] = new_log_pw

            new_root_log_pw = new_log_weighted_evidence_by_node_id[id(self.root_node)]
            candidate_log_probs.append(new_root_log_pw - current_log_pw)

        # normalize
        maximum_log = max(candidate_log_probs)
        exp_values = [math.exp(v - maximum_log) for v in candidate_log_probs]
        total = sum(exp_values)
        return [v / total for v in exp_values]

    def predict_sequence(self, sequence: list[int] | tuple[int, ...]) -> list[list[float]]:
        past_context: list[int] = []
        predicted_distributions: list[list[float]] = []

        for time_index, observed_symbol in enumerate(sequence):
            if not (0 <= observed_symbol < self.alphabet_size):
                raise ValueError(
                    f"Sequence symbol at index {time_index} is {observed_symbol}, "
                    f"out of range [0, {self.alphabet_size - 1}]."
                )

            predicted_distributions.append(self.predict(past_context))
            self.update(observed_symbol, past_context)

            past_context.insert(0, observed_symbol)
            if len(past_context) > self.maximum_depth:
                past_context = past_context[: self.maximum_depth]

        return predicted_distributions


if __name__ == "__main__":
    context_tree = ContextTree(maximum_depth=3, alphabet_size=2)

    sequence = [1, 0, 1, 0, 1, 1, 1, 1, 0]
    distributions = context_tree.predict_sequence(sequence)

    for index, distribution in enumerate(distributions):
        print(f"t={index:2d}  CTW prediction = {distribution}")
