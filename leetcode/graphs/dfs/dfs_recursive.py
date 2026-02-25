class DFS:
    def __init__(self, graph):
        self.graph = graph

    def dfs_recursive(self, first_node, visited=None):
        
        if visited is None:
            visited = set()

        if first_node not in visited:
            visited.add(first_node)

            for neighbor in self.graph[first_node]:
                self.dfs_recursive(neighbor, visited)
            

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity: O(V) for the visited set and O(V) for the recursion stack in the worst case.