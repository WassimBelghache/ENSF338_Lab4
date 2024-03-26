class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != i:
            parent[i] = self.find_parent(parent, parent[i]) 
        return parent[i]

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    def is_cycle(self):
        parent = [-1] * self.V
        for i in self.graph:
            x = self.find_parent(parent, i[0])
            y = self.find_parent(parent, i[1])
            if x == y:
                return True
            self.union(parent, x, y)
        return False

    def mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        for node in range(self.V):
            parent.append(node)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, x, y)
        mst_graph = Graph(self.V)
        for u, v, weight in result:
            mst_graph.add_edge(u, v, weight)
        return mst_graph

# Example:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst_graph = g.mst()
print("MST Edges:")
for u, v, weight in mst_graph.graph:
    print(f"{u} - {v}: {weight}")
