"""heap.py - implementation of a heap priority queue. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-17"

from enum import Enum


class HeapType(Enum):
    maxheap = 1
    minheap = 2


class HeapQueue:
    def __init__(self, initial_data, heap_type=HeapType.maxheap):
        self.data = []

    def build_heap(self, initial_data):
        pass

    def push(self, item):
        pass

    def peek(self):
        pass

    def pop(self):
        pass

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*heap*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

