import unittest
import sys
import os.path
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import nqueens


class NQueensTest(unittest.TestCase):

    def testDiagsValid(self):
        good_board = np.array([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
        self.assertTrue(nqueens.diags_valid(good_board))

        bad_board = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.assertFalse(nqueens.diags_valid(bad_board))

        bad_board2 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self.assertFalse(nqueens.diags_valid(bad_board2))

if __name__ == '__main__':
    unittest.main()

