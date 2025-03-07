#Uses python3

import sys

def reach(adj, x, y, visited):
    explore(adj, x, visited)
    if visited[y]:
        return 1
    return 0

def explore(adj, v, visited):
    visited[v] = True
    for vertix in adj[v]:
        if not visited[vertix]:
            explore(adj, vertix, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [False for _ in range(n)]
    print(reach(adj, x, y, visited))
