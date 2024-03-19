class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        self.edges[node] = []
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        for edge in self.edges.values():
            edge[:] = [x for x in edge if x[0] != node]
        del self.edges[node]

    def addEdge(self, n1, n2, weight=1):
        self.edges[n1].append((n2, weight))
        self.edges[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        self.edges[n1][:] = [x for x in self.edges[n1] if x[0] != n2]
        self.edges[n2][:] = [x for x in self.edges[n2] if x[0] != n1]

    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        if not lines[0].startswith('strict graph'):
            return None
        self.nodes.clear()
        self.edges.clear()
        for line in lines[1:-1]:
            n1, _, n2, weight = line.split()
            weight = int(weight[8:-1]) if 'weight' in weight else 1
            n1 = self.addNode(n1)
            n2 = self.addNode(n2)
            self.addEdge(n1, n2, weight)