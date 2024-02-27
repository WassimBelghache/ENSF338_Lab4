import time
import random
import matplotlib.pyplot as plt

# Inefficient Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Worst-case Complexity:
# Linear Search: O(n)
# Binary Search: O(log n)

def measure_time(func, arr, target, num_repetitions):
    times = []
    for _ in range(num_repetitions):
        start_time = time.time()
        func(arr, target)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def generate_sorted_array(size):
    arr = list(range(size))
    random.shuffle(arr)
    arr.sort()
    return arr

def compare_search_algorithms():
    num_elements = 1000
    num_repetitions = 100
    
    arr = generate_sorted_array(num_elements)

    target_value = arr[random.randint(0, num_elements - 1)]

    times_linear = measure_time(linear_search, arr, target_value, num_repetitions)
    times_binary = measure_time(binary_search, arr, target_value, num_repetitions)

    plt.figure(figsize=(10, 6))
    plt.hist(times_linear, label="Linear Search", alpha=0.7)
    plt.hist(times_binary, label="Binary Search", alpha=0.7)
    plt.xlabel("Execution Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Execution Times for Searching Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    compare_search_algorithms()