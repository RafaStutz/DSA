from collections import deque

class BFS:
    """
    Breadth-First Search (BFS) implementation for graph traversal.
    graph: A dictionary where keys are node identifiers and values are lists of neighboring nodes.
    start: The starting node for BFS traversal.
    order: A list to keep track of the order of visited nodes.
    visited: A set to keep track of visited nodes to avoid cycles.
    queue: A deque (double-ended queue) to manage the nodes to be explored next.
    """
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start):

        if start not in self.graph:
            raise KeyError(f"Start node {start!r} not in graph")

        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            
        return order

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for the visited set and the queue.
