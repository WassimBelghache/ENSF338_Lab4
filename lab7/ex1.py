import random
import timeit
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value, parent_node=None, left_node=None, right_node=None):
        self.parent_node = parent_node
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert_node(self, value):
        if not self.root_node:
            self.root_node = TreeNode(value)
            return
        
        current_node = self.root_node
        while True:
            parent_node = current_node
            if value < current_node.value:
                if not current_node.left_node:
                    current_node.left_node = TreeNode(value, parent_node=current_node)
                    break
                current_node = current_node.left_node
            else:
                if not current_node.right_node:
                    current_node.right_node = TreeNode(value, parent_node=current_node)
                    break
                current_node = current_node.right_node

    def search_node(self, value):
        current_node = self.root_node
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left_node
            else:
                current_node = current_node.right_node
        return False

    def max_balance(self):
        max_balance_value = 0
        node_stack = [(self.root_node, 0)]
        while node_stack:
            node, depth_value = node_stack.pop()
            if node:
                current_balance_value = depth_value - min(self._depth(node.left_node), depth_value)
                max_balance_value = max(max_balance_value, current_balance_value)
                node_stack.append((node.right_node, depth_value + 1))
                node_stack.append((node.left_node, depth_value + 1))
        return max_balance_value

    def _depth(self, node):
        if not node:
            return 0
        depth_value = 0
        while node:
            depth_value += 1
            node = node.right_node
        return depth_value

bst = BinarySearchTree()
for i in range(1000):
    bst.insert_node(i)

time_values = []
balance_values = []
for _ in range(1000):
    task_list = list(range(1000))
    random.shuffle(task_list)
    start_time_value = timeit.default_timer()
    for item in task_list:
        bst.search_node(item)
    end_time_value = timeit.default_timer()
    time_values.append(end_time_value - start_time_value)
    balance_values.append(bst.max_balance())

plt.scatter(balance_values, time_values)
plt.title('Scatter plot of Absolute Balance vs Search Time')
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (seconds)')
plt.show()
