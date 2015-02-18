"""heap.py - implementation of a heap priority queue. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-17"

from enum import Enum
from autoresizelist import AutoResizeList


class HeapType(Enum):
    maxheap = 1
    minheap = 2


class Heap:
    def __init__(self, initial_data=None, heap_type=HeapType.maxheap):
        if initial_data is None:
            self.data = AutoResizeList()
        else:
            self.data = AutoResizeList(initial_data)

        self.heap_type = heap_type
        self.build_heap(initial_data)

    def _left_child(self, index):
        return 2*index + 1

    def _right_child(self, index):
        return 2*index + 2

    def _resize_if_necessary(self):
        pass

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

