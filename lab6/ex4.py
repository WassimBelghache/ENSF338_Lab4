class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self._heapify_down(i)

    def enqueue(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return top

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)


import random
import unittest

class TestHeap(unittest.TestCase):
    def test_heapify_sorted(self):
        heap = Heap()
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        heap.heapify(input_arr)
        self.assertEqual(heap.heap, [7, 5, 6, 4, 2, 1, 3])

    def test_heapify_empty(self):
        heap = Heap()
        input_arr = []
        heap.heapify(input_arr)
        self.assertEqual(heap.heap, [])

    def test_heapify_random(self):
        heap = Heap()
        input_arr = random.sample(range(1, 100), 50)
        heap.heapify(input_arr)
        for i in range(len(heap.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap.heap):
                self.assertTrue(heap.heap[i] >= heap.heap[left])
            if right < len(heap.heap):
                self.assertTrue(heap.heap[i] >= heap.heap[right])


if __name__ == '__main__':
    unittest.main() 