from DFS import dfs


def w(u, v):
    return W[u][v]

def try_to_relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u

def DAG_Relaxation(Adj, w, s):
    _, order = dfs(Adj, s)
    order.reverse()
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    for u in order:
        for v in Adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)
    return d, parent
W ={0: {1: 4},
    1: {2: 3},
    2: {3: 2},
    3: {4: -5, 5: 1},
    4: {5: 0},
    5: {}}
Adj =  [[1],
        [2],
        [3],
        [4, 5],
        [5],
        []]
print(DAG_Relaxation(Adj, w, 0))