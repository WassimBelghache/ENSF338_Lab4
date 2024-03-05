import random
import timeit

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

#Sorted vector
sorted_vector = list(range(10000))
random.shuffle(sorted_vector) 
bst_sorted = BST()
for key in sorted_vector:
    bst_sorted.insert(key)

def measure_search_performance_sorted(bst):
    total_time = 0
    for key in sorted_vector:
        avg_time = timeit.timeit(lambda: bst.search(key), number=10) / 10
        total_time += avg_time
    return total_time / len(sorted_vector), total_time

avg_time_sorted, total_time_sorted = measure_search_performance_sorted(bst_sorted)

#Shuffled vector
bst_shuffled = BST()
for key in sorted_vector:
    bst_shuffled.insert(key)

def measure_search_performance_shuffled(bst):
    total_time = 0
    for key in sorted_vector:
        avg_time = timeit.timeit(lambda: bst.search(key), number=10) / 10
        total_time += avg_time
    return total_time / len(sorted_vector), total_time

random.shuffle(sorted_vector)
avg_time_shuffled, total_time_shuffled = measure_search_performance_shuffled(bst_shuffled)

# Results
print("Sorted Vector:")
print("Average time per search:", avg_time_sorted)
print("Total time for all searches:", total_time_sorted)

print("\nShuffled Vector:")
print("Average time per search:", avg_time_shuffled)
print("Total time for all searches:", total_time_shuffled)

#4
'''The search performance is faster for the sorted vector approach.This is because in a balanced binary search tree, 
the height is minimized, leading to faster search times. However, in the shuffled vector approach, the tree becomes less 
balanced, increasing the height of the tree and thus increasing the search time.'''
