import unittest
import sys
import os.path
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import heap


def is_heap(h):
    sorted_data = list(sorted(filter(lambda x: x is not None, h.data), reverse=True))
    pop_order = [h.pop() for _ in range(h.size())]
    print("\nsorted data: {0}\npop_order:   {1}".format(sorted_data, pop_order))
    return sorted_data == pop_order


class HeapTest(unittest.TestCase):
    def testMaxHeapPushPop(self):
        # Test push
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

        # Test peek
        self.assertEqual(h.peek(), 21)

        # Test pop
        self.assertEqual(h.pop(), 21)
        self.assertEqual(h.pop(), 20)
        self.assertEqual(h.pop(), 9)
        self.assertEqual(h.pop(), 7)

        # Larger test
        data = [93, 89, 91, 84, 87, 54, 71, 62, 75, 35, 43, 50, 77, 27, 14, 42, 13, 35, 10, 4]
        h2 = heap.Heap()
        for d in data:
            h2.push(d)

        self.assertTrue(is_heap(h2))

    def testMinHeapPushPop(self):
        # Test Push
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

        # Test peek
        self.assertEqual(h.peek(), -1)

        # Test pop
        self.assertEqual(h.pop(), -1)
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(h.pop(), 5)
        h.push(-10)
        self.assertEqual(h.pop(), -10)

    def testMaxHeapBuild(self):
        data = [98, 45, 69, 85, 34, 66, 10, 2, 11, 3, 21, 30, 91, 32, 55, 74, 93, 17, 67, 19]
        h = heap.Heap(data)
        self.assertTrue(is_heap(h))

        # data2 = [random.randint(1, 100) for _ in range(20)]
        # print("\n\ndata:        {0}".format(data2))
        # h3 = heap.Heap(data2[:])
        # self.assertTrue(is_heap(h3))
        
if __name__ == '__main__':
    unittest.main()

