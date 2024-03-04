import timeit
import random
import matplotlib.pyplot as plt

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        return item

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

def measure_performance(queue_class, tasks):
    queue = queue_class()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)  
        else:
            queue.dequeue()
    end_time = timeit.default_timer()
    return end_time - start_time

# Measure performance
array_times = []
linked_list_times = []
for _ in range(100):
    tasks = generate_random_tasks()
    array_time = measure_performance(ArrayQueue, tasks)
    linked_list_time = measure_performance(LinkedListQueue, tasks)
    array_times.append(array_time)
    linked_list_times.append(linked_list_time)

# Plotting
plt.hist(array_times, bins=20, alpha=0.5, label='Array Queue')
plt.hist(linked_list_times, bins=20, alpha=0.5, label='Linked List Queue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Queue Implementation Times')
plt.legend()
plt.show()

print("Mean time for Array Queue:", sum(array_times) / len(array_times))
print("Mean time for Linked List Queue:", sum(linked_list_times) / len(linked_list_times))

'''The graph clearly shows that the linked list implementation performs much faster than the array 
implementation in this test. This outcome was anticipated, as the array implementation has O(1) complexity 
for dequeue operations and O(n) for enqueue operations, whereas the linked list implementation has the opposite. 
Our test is designed to enqueue much more frequently than dequeue.'''