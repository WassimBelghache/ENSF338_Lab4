import random
import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.data = value
        self.height = 1 

class Tree:
    def __init__(self):
        self.root_node = None

    def add_node(self, value):
        if not self.root_node:
            self.root_node = Node(value)
        else:
            self.root_node = self.place_node(self.root_node, value)

    def place_node(self, current, value):
        if not current:
            return Node(value)
        if value < current.data:
            current.left_child = self.place_node(current.left_child, value)
        else:
            current.right_child = self.place_node(current.right_child, value)

        current.height = 1 + max(self.node_height(current.left_child), self.node_height(current.right_child))

        balance = self.node_balance(current)

        # Case 1: Pivot does not exist
        if balance > 1 and value < current.left_child.data:
            print("Case #1: Pivot not detected")
            return self.right_rotate(current)

        # Case 2: Pivot exists, and a node was added to the shorter subtree
        if balance < -1 and value > current.right_child.data:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return self.left_rotate(current)

        return current

    def left_rotate(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self.node_height(z.left_child), self.node_height(z.right_child))
        y.height = 1 + max(self.node_height(y.left_child), self.node_height(y.right_child))
        return y

    def right_rotate(self, y):
        x = y.left_child
        T2 = x.right_child
        x.right_child = y
        y.left_child = T2
        y.height = 1 + max(self.node_height(y.left_child), self.node_height(y.right_child))
        x.height = 1 + max(self.node_height(x.left_child), self.node_height(x.right_child))
        return x

    def node_height(self, node):
        if not node:
            return 0
        return node.height

    def node_balance(self, node):
        if not node:
            return 0
        return self.node_height(node.left_child) - self.node_height(node.right_child)

# Test cases
tree = Tree()
tree.add_node(10)  
tree.add_node(20)  
tree.add_node(30)  
tree.add_node(40)  
