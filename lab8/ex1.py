#this code was written with the help of chatgpt

class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        return node

    def removeNode(self, node):
        del self.adjacency_list[node]
        for adj_list in self.adjacency_list.values():
            if node in adj_list:
                adj_list.remove(node)

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            return False
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))
        return True

    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            return False
        self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
        self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]
        return True

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                if not lines:
                    return None
                
                if 'strict graph' not in lines[0]:
                    return None
                
                self.adjacency_list = {}
                for line in lines[1:]:
                    line = line.strip()
                    if not line or line.startswith('}'):
                        break
                    nodes, attrs = line.split('[', 1) if '[' in line else (line, None)
                    node1, node2 = nodes.split('--')
                    node1 = node1.strip()
                    node2 = node2.strip()
                    weight = 1
                    if attrs:
                        weight = int(attrs.split('=')[1].strip()[:-1])
                    if node1 not in self.adjacency_list:
                        self.addNode(node1)
                    if node2 not in self.adjacency_list:
                        self.addNode(node2)
                    self.addEdge(node1, node2, weight)
                return True
        except FileNotFoundError:
            return None
        except Exception as e:
            print("Error:", e)
            return None

# Example usage:
g = Graph()

#adding nodes
node1 = g.addNode("node1")
node2 = g.addNode("node2")
node3 = g.addNode("node3")
node4 = g.addNode("node4")

print("Nodes after adding:")
print(g.adjacency_list)

#adding edges
g.addEdge(node1, node2, weight=5)
g.addEdge(node2, node3)
g.addEdge(node4, node3, weight=6)

print("Edges after adding:")
print(g.adjacency_list)

#removing node
g.removeNode(node4)

print("Nodes after removing node 4:")
print(g.adjacency_list)

#remoiving edge
g.removeEdge(node1, node2)

print("Edges after removing edge between node 1 and node 2:")
print(g.adjacency_list)

#importing graph from file
result = g.importFromFile("graphviz_file.txt")
print("Graph import result:", result)

print("Graph after importing from file:")
print(g.adjacency_list)

