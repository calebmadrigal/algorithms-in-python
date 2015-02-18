import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from autoresizelist import AutoResizeList


class AutoResizeListTest(unittest.TestCase):

    def testSet(self):
        a = AutoResizeList()
        a[5] = 5
        self.assertEqual(a._data, [None, None, None, None, None, 5])

        b = AutoResizeList([0, 1, 2, 3], fill=0)
        b[6] = 6
        self.assertEqual(b._data, [0, 1, 2, 3, 0, 0, 6])

    def testGet(self):
        c = AutoResizeList([], fill=100)
        c[10] = 1
        self.assertEqual(c[10], 1)
        self.assertEqual(c[9], 100)

    def testDel(self):
        d = AutoResizeList([0, 1, 2])
        d[4] = 4
        del d[3]
        self.assertEqual(d._data, [0, 1, 2, 4])

    def testEqual(self):
        a = AutoResizeList([1, 2, 3])
        b = AutoResizeList([1, 2, 3])
        self.assertEqual(a, b)

    def testLen(self):
        a = AutoResizeList([1, 2, 3])
        self.assertEqual(len(a), 3)

    def testPrepend(self):
        a = AutoResizeList([1, 2, 3])
        a.prepend(0)
        self.assertEqual(0, a._data[0])

if __name__ == '__main__':
    unittest.main()

