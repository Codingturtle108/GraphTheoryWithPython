from collections import  defaultdict
def main():
    n = int(input())
    adj_list = defaultdict(list)

    # Reading the graph in adjacency list representation
    for i in range(n):
        adj_list[i] = list(map(int, input().split()))

    deg = [len(adj_list[i]) for i in range(n)]
    print(deg)

    # Check for Eulerian cycle possibility
    has_odd_degree = any(deg[i] % 2 != 0 for i in range(n))

    if has_odd_degree:
        print(-1)
        return

    stack = [0]
    res = []

    while stack:
        v = stack[-1]
        if not adj_list[v]:
            res.append(v)
            stack.pop()
        else:
            u = adj_list[v].pop()
            adj_list[u].remove(v)
            if u in adj_list[v]:
                adj_list[v].remove(u)
            stack.append(u)

    # Check if all edges have been traversed
    if any(adj_list[i] for i in range(n)):
        print(-1)
    else:
        print(*res)

if __name__ == "__main__":
    main()
