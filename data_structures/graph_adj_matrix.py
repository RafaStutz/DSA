class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def add_edge(self, i, j):
        self.graph[i][j] = 1
        self.graph[j][i] = 1 

# Time Complexity: O(1) for adding an edge.
# Space Complexity: O(V^2) where V is the number of vertices.
# Good for dense graphs.