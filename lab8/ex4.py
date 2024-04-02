#This code was written with the help of chatGPT

import re
import timeit
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def addNode(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
    
    def removeNode(self, data):
        if data in self.adjacency_list:
            del self.adjacency_list[data]
            for key, value in self.adjacency_list.items():
                self.adjacency_list[key] = [v for v in value if v[0] != data]

    def addEdge(self, n1, n2, weight=1):
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
        self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]

    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        if not lines[0].strip() == "strict graph G {":
            return None

        self.adjacency_list.clear()

        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1

            self.addNode(node1_data)
            self.addNode(node2_data)
            self.addEdge(node1_data, node2_data, weight)

        return self
    
    def dfs(self, start_node):
        visited = set()
        traversal = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for neighbor, _ in self.adjacency_list[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return traversal

# Create a new Graph instance
graph1 = Graph()

# Add nodes to the graph
graph1.addNode("1")
graph1.addNode("2")
graph1.addNode("3")
graph1.addNode("4")

# Add edges to the graph
graph1.addEdge("1", "2")
graph1.addEdge("1", "3")
graph1.addEdge("2", "4")

# Perform a DFS traversal
traversal = graph1.dfs("1")

# Print the traversal
print(traversal)

# Import graph from file
graph2 = Graph()
graph2.importFromFile("random.dot")
start_node = list(graph2.adjacency_list.keys())[0]  # or any node of your choice

# Measure time for DFS traversal
def graphTime():
    graph2.dfs(start_node)

times = timeit.repeat(graphTime, number=10)
print("Time for graph of adjacency list:")
print(f"Maximum time: {max(times)}")
print(f"Minimum time: {min(times)}")
print(f"Average time: {sum(times) / len(times)}")

class Graph2:
    def __init__(self):
        self.nodes = []
        self.adjacency_matrix = []

    def addNode(self, data):
        if data not in self.nodes:
            self.nodes.append(data)
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * len(self.nodes))

    def getNodeIndex(self, node):
        return self.nodes.index(node) if node in self.nodes else None

    def addEdge(self, n1, n2, weight=1):
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
            self.nodes.remove(node)
            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)

    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        if not lines[0].strip() == "strict graph G {":
            return None

        self.nodes.clear()
        self.adjacency_matrix.clear()

        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1

            if node1_data not in self.nodes:
                self.addNode(node1_data)
            if node2_data not in self.nodes:
                self.addNode(node2_data)

            self.addEdge(node1_data, node2_data, weight)

        return self
    
    def dfs(self, start_node):
        visited = set()
        traversal = []

        def dfs_recursive(node):
            index = self.getNodeIndex(node)
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for i, weight in enumerate(self.adjacency_matrix[index]):
                    if weight != 0:
                        dfs_recursive(self.nodes[i])

        dfs_recursive(start_node)
        return traversal

# Create a new Graph2 instance
graph3 = Graph2()

# Add nodes to the graph
graph3.addNode("1")
graph3.addNode("2")
graph3.addNode("3")
graph3.addNode("4")

# Add edges to the graph
graph3.addEdge("1", "2")
graph3.addEdge("1", "3")
graph3.addEdge("2", "4")

# Perform a DFS traversal
traversal = graph3.dfs("1")

# Print the traversal
print(traversal)  # Output: ['1', '2', '4', '3']

# Import graph from file
graph4 = Graph2()
graph4.importFromFile("random.dot")
start_node = graph4.nodes[0]

# Measure time for DFS traversal
def graphTime2():
    graph4.dfs(start_node)

time2 = timeit.repeat(graphTime2, number=10)

# Print the maximum, minimum, and average time
print("Time for graph of adjacency matrix:")
print(f"Maximum time: {max(time2)}")
print(f"Minimum time: {min(time2)}")
print(f"Average time: {sum(time2) / len(time2)}")

# Q3
# Adjacency Matrix:
# Conversely, the adjacency matrix represents the graph as a 2D array. 
# Identifying node neighbors requires scanning an entire row or column, taking O(V) time, where V denotes vertices. 
# Consequently, even nodes with few neighbors necessitate scanning the entire row/column. 
# As a result, DFS on an adjacency matrix exhibits a time complexity of O(V^2).

# Adjacency List:
# In this representation, each node keeps track of its adjacent nodes, simplifying neighbor iteration, crucial for DFS. 
# The time complexity for DFS on an adjacency list is O(V + E), where V represents vertices and E represents edges. 
# This complexity arises because each vertex and edge are traversed exactly once.
