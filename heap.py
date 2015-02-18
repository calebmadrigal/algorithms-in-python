"""heap.py - implementation of a heap priority queue. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-17"

from enum import Enum


class HeapType(Enum):
    maxheap = 1
    minheap = 2


class Heap:
    def __init__(self, initial_data, heap_type=HeapType.maxheap):
        self.heap_type = heap_type
        self.data = []
        self.build_heap(initial_data)

    def build_heap(self, initial_data):
        for i in initial_data:
            self.data.append(i)

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[0]

    def pop(self):
        item = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        return item

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*heap*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

