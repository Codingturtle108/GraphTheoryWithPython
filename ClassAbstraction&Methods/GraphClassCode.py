class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adjlist = self.adj_list()
        print(self.adjlist)
    def add_vertex(self, vertex):
        self.nodes.append(vertex)
        self.adjlist[vertex]=[]
        print(self.nodes)
        print(self.adjlist)
    def add_edge(self, edge):
        self.edges.append(edge)
        node1, node2 = edge[0], edge[1]
        self.adjlist[node1].append(node2)
        print(self.edges)
        print(self.adjlist)
    def adj_list(self):
        adj_list = {node: [] for node in self.nodes}
        for edge in self.edges:
            node1, node2 = edge[0], edge[1]
            adj_list[node1].append(node2)
        return adj_list
    def count_outdegree(self):
        outdegree = {}
        for v in self.nodes:
            outdegree[v] = len(self.adjlist[v])
        print(outdegree)
    def count_indegree(self):
        indegree ={node:0 for node in self.nodes}
        for vertex in self.nodes:
            for node in self.adjlist[vertex]:
                indegree[node] +=1
        print(indegree)

G = Graph([1,2,3,4],[(2,4),(3,2),(2,1),(1,3),(4,1)])
G.add_vertex(5)
G.add_edge((1,5))
G.count_outdegree()
G.count_indegree()