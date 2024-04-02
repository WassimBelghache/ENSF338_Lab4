import re
import timeit

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
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for nodes in self.adjacency_list.values():
                if node in nodes:
                    nodes.remove(node)

    def addEdge(self, n1, n2, weight = 1):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1].append((n2, weight))
            self.adjacency_list[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
            self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]
    
    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        # Check if the graph is undirected
        if not lines[0].strip() == "strict graph G {":
            return None
        # Clear existing nodes and edges
        self.adjacency_list.clear()
        # Parse edges
        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1
            node1 = self.addNode(node1_data)
            node2 = self.addNode(node2_data)
            self.addEdge(node1, node2, weight)

        return self
    
    def dfs(self, start_node):
        visited = set()
        traversal = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                traversal.append(node.data)
                for neighbor, _ in self.adjacency_list[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return traversal

class Graph2:
    def __init__(self):
        self.nodes = []
        self.adjacency_matrix = []

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes.append(node)

        # Add a new row and column in the adjacency matrix for the new node
        if self.adjacency_matrix:
            for row in self.adjacency_matrix:
                row.append(0)
        self.adjacency_matrix.append([0] * len(self.nodes))

        return node

    def getNodeIndex(self, node):
        for i, n in enumerate(self.nodes):
            if n == node:
                return i
        return None

    def addEdge(self, n1, n2, weight = 1):
        index1 = self.getNodeIndex(n1)
        index2 = self.getNodeIndex(n2)

        if index1 is not None and index2 is not None:
            self.adjacency_matrix[index1][index2] = weight
            self.adjacency_matrix[index2][index1] = weight

    def removeEdge(self, n1, n2):
        index1 = self.getNodeIndex(n1)
        index2 = self.getNodeIndex(n2)

        if index1 is not None and index2 is not None:
            self.adjacency_matrix[index1][index2] = 0
            self.adjacency_matrix[index2][index1] = 0

    def removeNode(self, node):
        index = self.getNodeIndex(node)

        if index is not None:
            # Remove the node from the node list
            self.nodes.remove(node)

            # Remove the corresponding row and column from the adjacency matrix
            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)
    
    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        # Check if the graph is undirected
        if not lines[0].strip() == "strict graph G {":
            return None

        # Clear existing nodes and edges
        self.nodes.clear()
        self.adjacency_matrix.clear()

        # Parse edges
        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1

            # Check if nodes already exist, if not create them
            node1 = next((node for node in self.nodes if node.data == node1_data), None)
            if node1 is None:
                node1 = self.addNode(node1_data)

            node2 = next((node for node in self.nodes if node.data == node2_data), None)
            if node2 is None:
                node2 = self.addNode(node2_data)

            self.addEdge(node1, node2, weight)

        return self
    
    def dfs(self, start_node):
        visited = set()
        traversal = []

        def dfs_recursive(node):
            index = self.getNodeIndex(node)
            if node not in visited:
                visited.add(node)
                traversal.append(node.data)
                for i, weight in enumerate(self.adjacency_matrix[index]):
                    if weight != 0:
                        dfs_recursive(self.nodes[i])

        dfs_recursive(start_node)
        return traversal


# Create a new Graph instance
graph1 = Graph()

# Add nodes to the graph
node1 = graph1.addNode("1")
node2 = graph1.addNode("2")
node3 = graph1.addNode("3")
node4 = graph1.addNode("4")

# Add edges to the graph
graph1.addEdge(node1, node2)
graph1.addEdge(node1, node3)
graph1.addEdge(node2, node4)

# Perform a DFS traversal
traversal = graph1.dfs(node1)

# Print the traversal
print(traversal)  # Output: ['1', '2', '4', '3']

# Create a new Graph2 instance
graph2 = Graph2()

# Add nodes to the graph
node1 = graph2.addNode("1")
node2 = graph2.addNode("2")
node3 = graph2.addNode("3")
node4 = graph2.addNode("4")

# Add edges to the graph
graph2.addEdge(node1, node2)
graph2.addEdge(node1, node3)
graph2.addEdge(node2, node4)

# Perform a DFS traversal
traversal = graph2.dfs(node1)

# Print the traversal
print(traversal)  # Output: ['1', '2', '4', '3']

# Q3
# Using the adjacency list
graph3 = Graph()
graph3.importFromFile("random.dot")
start_node = list(graph3.adjacency_list.keys())[0]  # or any node of your choice
def graphTime():
    graph3.dfs(start_node)

times = timeit.repeat(graphTime, number=10)
print("Time for graph of adjacency list:")
print(f"Maximum time: {max(times)}")
print(f"Minimum time: {min(times)}")
print(f"Average time: {sum(times) / len(times)}")

# Using the adjacency matrix
graph4 = Graph2()
graph4.importFromFile("random.dot")
start_node = graph4.nodes[0]

def graphTime2():
    graph4.dfs(start_node)

time2 = timeit.repeat(graphTime2, number=10)

# Print the maximum, minimum, and average time
print("Time for graph of adjacency matrix:")
print(f"Maximum time: {max(time2)}")
print(f"Minimum time: {min(time2)}")
print(f"Average time: {sum(time2) / len(time2)}")

'''
Q3
Time for graph of adjacency list is faster than that of the adjacency matrix.

Adjacency List: In an adjacency list, each node maintains a list of its adjacent nodes. This makes it very 
efficient to iterate over the neighbors of a particular node, which is a common operation in depth-first search (DFS). 
The DFS algorithm for an adjacency list representation runs in O(V + E) time, where V is the number of vertices and E is the 
number of edges. This is because each vertex and each edge will be explored exactly once.

Adjacency Matrix: In an adjacency matrix, the graph is represented as a 2D array. To find the neighbors of a node, 
you need to scan an entire row (or column), which takes O(V) time, where V is the number of vertices. Therefore, even 
if a node has only a few neighbors, you still need to scan all the entries in a row or column. This makes the DFS algorithm 
for an adjacency matrix representation run in O(V^2) time.
'''