import time
import random
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def binary_search(self, num):
        left = 0
        right = self.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.get(mid).data == num:
                return mid
            elif self.get(mid).data < num:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class Array:
    def __init__(self):
        self.arr = []

    def insert(self, data):
        self.arr.append(data)

    def binary_search(self, num):
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == num:
                return mid
            elif self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return -1

def measure_performance(data_structure, input_sizes):
    average_times = []
    for size in input_sizes:
        total_time = 0
        for _ in range(10):
            data = sorted(random.sample(range(size * 10), size)) 
            start_time = time.time()
            for num in data:
                data_structure.binary_search(num)
            end_time = time.time()
            total_time += (end_time - start_time)
        average_time = total_time / 10 
        average_times.append(average_time)
    return average_times

input_sizes = [1000, 2000, 4000, 8000]

linked_list_performance = measure_performance(LinkedList(), input_sizes)

array_performance = measure_performance(Array(), input_sizes)

plt.plot(input_sizes, linked_list_performance, label='Linked List')
plt.plot(input_sizes, array_performance, label='Array')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Binary Search Performance')
plt.legend()
plt.show()