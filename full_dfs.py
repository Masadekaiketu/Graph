from DFS import dfs
def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order) #each connected component is stored in order as list
    return parent, order

Adj =  [[1, 2],
        [2],
        [3],
        [3]]
print(full_dfs(Adj))