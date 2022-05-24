from DFS import dfs
def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in Adj.keys():
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order
