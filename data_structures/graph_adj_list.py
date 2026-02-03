class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, i, j):
        self.graph[i].append(j)
        self.graph[j].append(i)

# Time Complexity: O(1) for adding an edge.
# Space Complexity: O(V + E) where V is vertices and E is edges.
# Good for sparse graphs.