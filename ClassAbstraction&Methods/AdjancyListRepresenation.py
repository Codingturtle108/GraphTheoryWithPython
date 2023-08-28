nodes = [1,2,3,4]
edges = [(1,2),(2,3)]
def adj_list(nodes,edges):
    adj_dict  ={node:[] for node in nodes}
    for edge in edges:
        node1,node2 = edge[0],edge[1]
        adj_dict[node1].append(node2)
        adj_dict[node2].append(node1)
    print(adj_dict)
adj_list(nodes,edges)