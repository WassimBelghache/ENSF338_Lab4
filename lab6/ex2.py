import timeit
import random

# BST Implementation
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.val:
            if not current_node.left:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if not current_node.right:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if not current_node:
            return False
        if key == current_node.val:
            return True
        elif key < current_node.val:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

# Binary Search Implementation
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Generate, shuffle, and use vector to build a BST
vector = list(range(10000))
random.shuffle(vector)
bst = BST()
for num in vector:
    bst.insert(num)

# Measure BST search performance
bst_search_times = [timeit.timeit(lambda: bst.search(x), number=10) for x in vector]
avg_bst_search_time = sum(bst_search_times) / len(bst_search_times)
total_bst_search_time = sum(bst_search_times)

# Sort the vector for binary search
sorted_vector = sorted(vector)

# Measure binary search performance
binary_search_times = [timeit.timeit(lambda: binary_search(sorted_vector, x), number=10) for x in vector]
avg_binary_search_time = sum(binary_search_times) / len(binary_search_times)
total_binary_search_time = sum(binary_search_times)

# Results
print(f'BST Search - Average Time: {avg_bst_search_time}, Total Time: {total_bst_search_time}')
print(f'Binary Search - Average Time: {avg_binary_search_time}, Total Time: {total_binary_search_time}')
