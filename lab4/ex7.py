#Coded with help of chatGPT

import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current

    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def reverse_optimized(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next  
            current_node.next = prev_node  
            prev_node = current_node  
            current_node = next_node  

        self.head = prev_node  

# Create a list with 1000, 2000, 3000, 4000 elements
sizes = [1000, 2000, 3000, 4000]
num_trials = 100

# Time the reverse method
reverse_times = []
for size in sizes:
    linked_list = LinkedList()
    for i in range(size):
        linked_list.add(i)
    time_taken = timeit.timeit(lambda: linked_list.reverse(), number=num_trials)
    reverse_times.append(time_taken / num_trials)

# Time the reverse_optimized method
reverse_optimized_times = []
for size in sizes:
    linked_list = LinkedList()
    for i in range(size):
        linked_list.add(i)
    time_taken = timeit.timeit(lambda: linked_list.reverse_optimized(), number=num_trials)
    reverse_optimized_times.append(time_taken / num_trials)

# Plot the results
plt.plot(sizes, reverse_times, label='reverse')
plt.plot(sizes, reverse_optimized_times, label='reverse_optimized')
plt.xlabel('List size (log scale)')
plt.ylabel('Time (s)')
plt.xscale('log')
plt.legend()
plt.show()

