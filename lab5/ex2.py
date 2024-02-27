class PriorityQueueMergesort:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        self.queue.sort()  # Sort using mergesort

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Priority queue is empty")


#2 Priority Queue with Sorted Insertion:
class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        self.queue.sort()  # Sort using mergesort

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Priority queue is empty")



#3 Generating Random Lists of Tasks:

import random

def generate_random_task_list(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

#4
import timeit

def generate_random_task_list(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

def measure_performance(pq_class, task_list):
    pq = pq_class()
    for task in task_list:
        if task == "enqueue":
            pq.enqueue(random.randint(1, 100))  # Example: Enqueue random integer
        else:
            pq.dequeue()

if __name__ == "__main__":
    num_lists = 100
    num_tasks_per_list = 1000

    random_task_lists = [generate_random_task_list(num_tasks_per_list) for _ in range(num_lists)]

    # Measure performance for PriorityQueueMergesort
    mergesort_time = timeit.timeit(lambda: measure_performance(PriorityQueueMergesort, random_task_lists), number=1)
    print(f"PriorityQueueMergesort execution time: {mergesort_time:.6f} seconds")

    # Measure performance for PriorityQueueSortedInsert
    sorted_insert_time = timeit.timeit(lambda: measure_performance(PriorityQueueSortedInsert, random_task_lists), number=1)
    print(f"PriorityQueueSortedInsert execution time: {sorted_insert_time:.6f} seconds")

#5 
    '''the PriorityQueue Insert implementation is expected to be faster because it avoids sorting the entire 
    array after each enqueue operation, instead only inserting the new element in the correct position.'''
    



