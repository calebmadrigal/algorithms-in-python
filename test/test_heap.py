import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import heap


class HeapTest(unittest.TestCase):

    def testMaxPushHeap(self):
        h = heap.Heap()
        h.push(5).push(3).push(9).push(1)
        self.assertEqual(str(h), "[9, 3, 5, 1]")

        h.push(20)
        self.assertEqual(str(h), "[20, 9, 5, 1, 3]")

        h.push(2)
        self.assertEqual(str(h), "[20, 9, 5, 1, 3, 2]")

        h.push(7)
        self.assertEqual(str(h), "[20, 9, 7, 1, 3, 2, 5]")

        h.push(21)
        self.assertEqual(str(h), "[21, 20, 7, 9, 3, 2, 5, 1]")

    def testMinPushHeap(self):
        h = heap.Heap([], heap.HeapType.minheap)
        h.push(5)
        self.assertEqual(str(h), "[5]")

        h.push(7)
        self.assertEqual(str(h), "[5, 7]")

        h.push(3)
        self.assertEqual(str(h), "[3, 7, 5]")

        h.push(4)
        self.assertEqual(str(h), "[3, 4, 5, 7]")

        h.push(-1)
        self.assertEqual(str(h), "[-1, 3, 5, 7, 4]")

        #data = [6, 1, 4, 9, 8, 2, 3]
        #h = heap.Heap(data, heap.HeapType.maxheap)
        #self.assertEqual(h.pop(), 9)
        #self.assertEqual(h.pop(), 8)
        #h.push(15)
        #h.push(0)
        #self.assertEqual(h.pop(), 15)
        
if __name__ == '__main__':
    unittest.main()

