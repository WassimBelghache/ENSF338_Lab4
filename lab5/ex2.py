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
            raise IndexError("Priority queue is empty")


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

# Example usage:
random_tasks = generate_random_task_list(1000)
print(random_tasks[:10])  # Print the first 10 tasks






