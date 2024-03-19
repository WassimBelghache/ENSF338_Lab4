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
        self.edges[data] = {}
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        del self.edges[node.data]
        for edge_list in self.edges.values():
            if node.data in edge_list:
                del edge_list[node.data]

    def addEdge(self, n1, n2, weight=1):
        if n1.data not in self.nodes or n2.data not in self.nodes:
            raise ValueError("Both nodes must exist in the graph")
        self.edges[n1.data][n2.data] = weight
        self.edges[n2.data][n1.data] = weight

    def removeEdge(self, n1, n2):
        if n1.data not in self.nodes or n2.data not in self.nodes:
            raise ValueError("Both nodes must exist in the graph")
        del self.edges[n1.data][n2.data]
        del self.edges[n2.data][n1.data]

    def importFromFile(self, file):
        self.nodes = {}
        self.edges = {}
        with open(file, 'r') as f:
            lines = f.readlines()
        if not lines:
            return None

        if not lines[0].startswith("strict graph"):
            return None

        for line in lines[1:]:
            if line.strip() and not line.startswith("//") and not line.startswith("}"):
                parts = line.split("--")
                if len(parts) != 2:
                    return None
                node1, node2 = parts
                node1 = node1.strip()
                node2_parts = node2.strip().split()
                if len(node2_parts) == 1:
                    node2 = node2_parts[0].strip(";")
                    weight = 1
                elif len(node2_parts) == 3 and node2_parts[1] == "[weight=":
                    node2 = node2_parts[0].strip()
                    weight = int(node2_parts[2].strip("];"))
                else:
                    return None
                if node1 not in self.nodes:
                    self.addNode(node1)
                if node2 not in self.nodes:
                    self.addNode(node2)
                self.addEdge(self.nodes[node1], self.nodes[node2], weight)
        return self
