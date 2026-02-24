class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in g[node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges, as we need to traverse all vertices and edges in the worst case.
# Space Complexity: O(V) for the visited set and the queue, where V is the number of vertices in the graph.

# We build an adjacency list representation of the graph from the given edges.
# We then perform a breadth-first search (BFS) starting from the source node.
# We use a queue to keep track of the nodes to explore and a set to keep track of visited nodes to avoid cycles.
# If we reach the destination node during our BFS, we return True. If we exhaust the queue without finding the destination, we return False.
