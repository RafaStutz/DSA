class DFS:
    def __init__(self, graph):
        self.graph = graph

    def dfs_iterative(self, first_node):
        visited = set()
        stack = [first_node]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)

            for neighbor in reversed(self.graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity: O(V) for the visited set and O(V) for the stack in the worst case.

