from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_euler_path(self, v, path):
        while self.graph[v]:
            # Visit the next adjacent vertex
            next_vertex = self.graph[v].pop()
            # Recursively call the function on the next vertex
            self.find_euler_path(next_vertex, path)
        # Add the current vertex to the path
        path.append(v)

    def is_eulerian(self):
        # Check if all non-zero degree vertices are connected
        for key in self.graph:
            if len(self.graph[key]) % 2 != 0:
                return False
        return True

    def find_eulerian_path(self):
        if not self.is_eulerian():
            return "No Eulerian path exists."

        start_vertex = list(self.graph.keys())[0]  # Start from any vertex
        path = []
        self.find_euler_path(start_vertex, path)

        # The path is constructed in reverse, so reverse it to get the correct order
        return path[::-1]

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

eulerian_path = g.find_eulerian_path()
if eulerian_path == "No Eulerian path exists.":
    print(eulerian_path)
else:
    print("Eulerian Path:", " -> ".join(map(str, eulerian_path)))
