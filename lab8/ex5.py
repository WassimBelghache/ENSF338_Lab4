
# Q1
# Topological sorting, achieved with the Depth-First Search (DFS) algorithm, involves two key steps. 
# First, DFS is applied to determine the finish time of each vertex in the graph. 
# Then, vertices are arranged in descending order based on their finish time, yielding the topological sorting. 
# This approach is favored for scheduling tasks in directed acyclic graphs (DAGs) due to DFS's ability to efficiently identify task dependencies.

#This code was written with the help of chatgpt

import re

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

    def addEdge(self, n1, n2, weight):
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

        if not lines[0].strip() == "strict graph G {":
            print("The file does not represent a valid undirected graph.")
            return None

        self.adjacency_list.clear()

        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                print("Failed to parse line:", line)
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1

            node1 = self.addNode(node1_data)
            node2 = self.addNode(node2_data)
            self.addEdge(node1, node2, weight)

        print("Graph imported successfully from", file)
        return self
    
    # Q2
    def isdag(self):
        visited = set()
        path = set()

        for node in self.adjacency_list:
            if node not in visited:
                if self._has_cycle(node, visited, path):
                    return False
        return True

    def _has_cycle(self, node, visited, path):
        visited.add(node)
        path.add(node)

        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                if self._has_cycle(neighbor, visited, path):
                    return True
            elif neighbor in path:
                return True

        path.remove(node)
        return False
    
    def toposort(self):
        if not self.isdag():
            print("The graph is not a directed acyclic graph (DAG). Topological sorting cannot be performed.")
            return None

        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for neighbour, _ in self.adjacency_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            stack.insert(0, node)

        for node in self.adjacency_list:
            if node not in visited:
                dfs(node)

        print("Topological sorting completed successfully.")
        return stack
    
    # Q3
    def toposort_dfs(self):
        if not self.isdag():
            print("The graph is not a directed acyclic graph (DAG). Topological sorting cannot be performed.")
            return None

        visited = set()
        stack = []

        for node in self.adjacency_list:
            if node not in visited:
                self._dfs(node, visited, stack)

        print("Topological sorting completed successfully.")
        return [node.data for node in stack[::-1]]  
    def _dfs(self, node, visited, stack):
        visited.add(node)

        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)

        stack.append(node)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.importFromFile("random.dot")
    topological_order = g.toposort()
    if topological_order is not None:
        print("Topological order:", topological_order)


