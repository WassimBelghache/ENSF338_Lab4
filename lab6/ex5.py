class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

#module for priority queue
import heapq
import random
import timeit

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    
    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

# Function to generate a random list of tasks
def generate_tasks(n=1000, enqueue_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            tasks.append(('enqueue', random.randint(0, 1000)))
        else:
            tasks.append(('dequeue', None))
    return tasks

# Function to process tasks with a given priority queue
def process_tasks(pq_class, tasks):
    pq = pq_class()
    for op, value in tasks:
        if op == 'enqueue':
            pq.enqueue(value)
        elif op == 'dequeue':
            pq.dequeue()

# tasks call to function
tasks = generate_tasks()

# execution time for ListPriorityQueue
list_pq_time = timeit.timeit('process_tasks(ListPriorityQueue, tasks)', globals=globals(), number=1)

# execution time for HeapPriorityQueue
heap_pq_time = timeit.timeit('process_tasks(HeapPriorityQueue, tasks)', globals=globals(), number=1)

print(f"ListPriorityQueue total time: {list_pq_time} seconds")
print(f"ListPriorityQueue average time per task: {list_pq_time / 1000} seconds")
print(f"HeapPriorityQueue total time: {heap_pq_time} seconds")
print(f"HeapPriorityQueue average time per task: {heap_pq_time / 1000} seconds")


'''
The HeapPriorityQueue performed faster in the execution. This could show that the heap-based implementation
is more efficient compared to the linked list implementation. The heap can insert a new element or remove the smallest element in
O(logn) time, where n is the number of elements in the heap. This efficiency can become significant as the number of elements
increases where as linked list has the complexity of O(n) for insertion and O(1) for deletion.  
'''