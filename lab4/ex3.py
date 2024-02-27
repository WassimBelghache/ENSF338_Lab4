'''
Question 1
The list makes more room when it's full. This is called over-allocation. This is done in 
the line of code (line 70): new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;. 
This line calculates the new size of the array by adding an eighth of the current size (newsize >> 3) 
and a small constant (6) to the current size (newsize). The result is then rounded down to 
the nearest multiple of 4 by bitwise and with the complement of 3 (& ~(size_t)3). This ensures 
that the allocated size is always a multiple of 4, which can be beneficial for memory alignment. 
If the new size is closer to the overallocated size than to the old size, the function rounds 
the new size up to the nearest multiple of 4. This is done in the lines of code (line 74-75): 
if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize)) and 
new_allocated = ((size_t)newsize + 3) & ~(size_t)3;. This is done to avoid overallocation 
when the new size is significantly larger than the old size.
'''

# 2
import sys
lst = []

# Store the initial size of the list
last_size = sys.getsizeof(lst)

# Loop from 0 to 63
for i in range(64):

    lst.append(i)

    # Get the current size of the list
    current_size = sys.getsizeof(lst)


    if current_size != last_size:
        print(f"Capacity changed after adding element {i}, new capacity is {current_size} bytes")
        # Update the last size
        last_size = current_size

# 3
import timeit
import numpy as np
import matplotlib.pyplot as plt
def grow_array(S):
    S = 52
    arr = [0] * S
    arr.append(1)

time_taken = []
for i in range(1000):
    time_taken.append(timeit.timeit(grow_array, number=1000)/1000)
time1 = np.array(time_taken)
plt.hist(time1, color='skyblue', edgecolor='black')


# 4
def grow2_array(S):
    S = 51
    arr = [0] * S
    arr.append(1)

time_taken2 = []
for i in range(1000):
    time_taken2.append(timeit.timeit(grow2_array, number=1000)/1000)
time2 = np.array(time_taken2)
plt.hist(time2, color='green', edgecolor='black', alpha=0.5)

plt.show()

'''
Question 5
While both increasing and decreasing the size of the array appear similar on the histogram, 
expanding the array actually takes a bit longer. This is because expanding an array might require 
memory reallocation, which involves locating contiguous memory for the additional elements.
'''