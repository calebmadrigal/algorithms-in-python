import unittest
import sys
import os.path
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import nqueens


class NQueensTest(unittest.TestCase):

    def testRowsValid(self):
        zero_board = np.zeros((3, 3))
        self.assertTrue(nqueens.rows_valid(zero_board))

        bad_board = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(nqueens.rows_valid(bad_board))

        bad_board2 = np.array([[1, 0, 0], [0, 0, 0], [0, 1, 1]])
        self.assertFalse(nqueens.rows_valid(bad_board2))

        rows_good_board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(nqueens.rows_valid(rows_good_board))

        rows_good_board2 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.assertTrue(nqueens.rows_valid(rows_good_board2))

    def testColsValid(self):
        good_board = np.zeros((3, 3))
        self.assertTrue(nqueens.cols_valid(good_board))

        bad_board = np.array([[0, 0, 0], [0, 1, 0], [0, 1, 0]])
        self.assertFalse(nqueens.cols_valid(bad_board))

    def testDiagsValid(self):
        good_board = np.array([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
        self.assertTrue(nqueens.diags_valid(good_board))

        bad_board = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.assertFalse(nqueens.diags_valid(bad_board))

        bad_board2 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self.assertFalse(nqueens.diags_valid(bad_board2))

    def testBoardValid(self):
        good_board = np.array([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
        self.assertTrue(nqueens.is_valid(good_board))
        
if __name__ == '__main__':
    unittest.main()

