import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import quicksort


class QuicksortTest(unittest.TestCase):

    def testSort(self):
        a = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(quicksort.quicksort(a), [1,2,3,4,5,6,7,8,9])

        b = [8,7,6,5,4,3,2,1]
        self.assertEqual(quicksort.quicksort(b), [1,2,3,4,5,6,7,8])

        c = [1,6,3,2,1,9,7,5,4,9]
        self.assertEqual(quicksort.quicksort(c), [1,1,2,3,4,5,6,7,9,9])

        
if __name__ == '__main__':
    unittest.main()

