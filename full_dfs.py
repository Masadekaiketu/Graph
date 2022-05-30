from DFS import dfs
def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order) #each connected component is stored in order as list #len(order) is the number of connected component
    return parent, order

Adj =  [[1],
        [2],
        [3],
        [4],
        [5],
        [],
        [7],
        [8],
        []]
print(full_dfs(Adj))