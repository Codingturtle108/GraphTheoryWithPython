from GraphClassCode import Graph

def find_eulerian_cycle(G):
    in_degree = G.count_indegree()

        # Check if all nodes have even degrees (for Eulerian cycle)
    for degree in in_degree.values():
        if degree % 2 != 0:
            return []

    def dfs(node, visited_edges):
        if len(visited_edges) == len(G.edges):
            return [node]

        for neighbor in G.adjlist[node]:
            if (node, neighbor) not in visited_edges and (neighbor, node) not in visited_edges:
                visited_edges.add((node, neighbor))
                cycle = dfs(neighbor, visited_edges)
                if cycle:
                    return [node] + cycle
                visited_edges.remove((node, neighbor))

            return []

        eulerian_cycle = dfs(G.nodes[0], set())
        if eulerian_cycle:
            return eulerian_cycle
        else:
            return []

# Example usage
nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'A')]

graph = Graph(nodes, edges)
eulerian_cycle = find_eulerian_cycle(graph)

if eulerian_cycle:
    print("Eulerian Cycle:", eulerian_cycle)
else:
    print("No Eulerian Cycle found.")

