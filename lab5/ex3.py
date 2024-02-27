import random
import timeit
import matplotlib.pyplot as plt

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            return None

    def is_empty(self):
        return self.head is None

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append('push')
        else:
            tasks.append('pop')
    return tasks

def measure_performance(stack_impl, tasks):
    stack = stack_impl()
    for task in tasks:
        if task == 'push':
            stack.push(1)  # Pushing 1 as an arbitrary item
        else:
            stack.pop()

array_times = []
linked_list_times = []

for _ in range(100):
    tasks = generate_random_tasks()
    
    time_array = timeit.timeit(lambda: measure_performance(ArrayStack, tasks), number=1)
    array_times.append(time_array)
    
    time_linked_list = timeit.timeit(lambda: measure_performance(LinkedListStack, tasks), number=1)
    linked_list_times.append(time_linked_list)

plt.hist(array_times, bins=10, alpha=0.5, label='ArrayStack')
plt.hist(linked_list_times, bins=10, alpha=0.5, label='LinkedListStack')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Stack Implementation Times')
plt.show()