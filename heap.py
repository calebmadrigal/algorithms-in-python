"""heap.py - implementation of a heap priority queue. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-17"

import math
from enum import Enum
from autoresizelist import AutoResizeList


class HeapType(Enum):
    maxheap = 1
    minheap = 2


class Heap:
    def __init__(self, initial_data=None, heap_type=HeapType.maxheap):
        self.heap_type = heap_type
        if heap_type == HeapType.maxheap:
            self.comparator = lambda x, y: x > y
        else:
            self.comparator = lambda x, y: x < y

        self.data = AutoResizeList()
        if initial_data is not None:
            self.build_heap(initial_data)

        self._size = len(self.data)

    def _left_child(self, index):
        return 2*index + 1

    def _right_child(self, index):
        return 2*index + 2

    def _parent(self, index):
        return math.floor((index - 1) / 2.0)

    def _is_root(self, index):
        return index == 0

    def _swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]

    def build_heap(self, initial_data):
        for i in initial_data:
            self.data.prepend(i)
            self.heap_down(0)

    def heap_up(self, index):
        # If we are at the root, return - we are done
        if self._is_root(index):
            return

        # Else, compare the current node with the parent node, and if this node should be higher
        # then the parent node, then swap and recursively call on the parent index
        parent_index = self._parent(index)
        if self.comparator(self.data[index], self.data[parent_index]):
            self._swap(index, parent_index)
            self.heap_up(parent_index)

    def heap_down(self, index):
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        try:
            left = self.data[left_index]
        except IndexError:
            left = None
        try:
            right = self.data[right_index]
        except IndexError:
            right = None

        # Find the largest child
        largest_child = left
        largest_child_index = left_index
        if left is not None and right is not None:
            if self.comparator(right, left):
                largest_child = right
                largest_child_index = right_index
        elif right is not None:
            largest_child = right
            largest_child_index = right_index

        # If the largest child is not None and is higher priority than the current, then swap
        # and recursively call on on the child index
        if largest_child is not None and self.comparator(largest_child, self.data[index]):
            self._swap(index, largest_child_index)
            self.heap_down(largest_child_index)

    def push(self, item):
        insert_index = self._size  # Insert at the end
        self._size += 1

        self.data[insert_index] = item
        self.heap_up(insert_index)

        return self

    def peek(self):
        return self.data[0]

    def pop(self):
        if len(self.data) < 1 or self.data[0] is None:
            return None

        # Take item from the root
        item = self.data[0]

        # Move the bottom-most, right-most item to the root
        self.data[0] = self.data[self._size-1]
        self.data[self._size-1] = None
        self._size -= 1

        self.heap_down(0)

        return item

    def size(self):
        return self._size

    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*heap*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
