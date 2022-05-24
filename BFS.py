def bfs(Adj, s):
    parent = [None for v in Adj] #Adj is adjavency list
    parent[s] = s                   
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:     
            for v in Adj[u]:    #for all u's adjacency vertex
                if parent[v] is None:   #v's parent is u
                    parent[v] = u
                    level[-1].append(v) #append to same level
    return parent

def unweighted_shortest_path(Adj, s, t):
    parent = bfs(Adj, s)
    if parent[t] is None:
        return None
    i = t
    path = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1]


Adj =  [[1, 4, 3],
        [0],
        [3],
        [0, 2],
        [0]]

print(bfs(Adj, 3))