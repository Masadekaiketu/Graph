
from DAG_relaxation import try_to_relax


def dijkstra(Adj, w, s):
    d = [float('inf') for v in Adj]
    parent = [None for v in Adj]
    d[s], parent[s] = 0, s
    Q = PriorityQueue()
    V = len(Adj)
    for v in range(V):
        Q.insert(v, d[v])
    for _ in range(V):
        u = Q.extract_min()
        for v in Adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)
            Q.decrease_key(v, d[v])
    return d, parent

class PriorityQueue:
    def __init__(self):
        self.A = {}
    
    def insert(self, label, key):
        self.A[label] = key
    
    def extract_min(self):
        min_label = None
        for label in self.A:
            if (min_label is None) or (self.A[label] < self.A[min_label]):
                min_label = label
        del self.A[min_label]
        return min_label
    
    def decrease_key(self, label, key):
        if (label in self.A) and (key < self.A[label]):
            self.A[label] = key