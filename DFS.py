def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
        if parent[v] != s:
            print(v, s)
            print("cycle detect!!")
    order.append(s)
    return parent, order
