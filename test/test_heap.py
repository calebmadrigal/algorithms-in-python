import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import heap


class HeapTest(unittest.TestCase):

    def testHeap(self):
        data = [6, 1, 4, 9, 8, 2, 3]
        h = heap.Heap(data, heap.HeapType.maxheap)
        self.assertEqual(h.pop(), 9)
        self.assertEqual(h.pop(), 8)
        h.push(15)
        h.push(0)
        self.assertEqual(h.pop(), 15)
        
if __name__ == '__main__':
    unittest.main()

