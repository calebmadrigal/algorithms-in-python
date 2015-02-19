""" N-Queens solutions. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-19"

import numpy as np


def right_to_left_diagonals_valid(board):
    """ Returns True if there is no more than 1 "1" in each right-to-left diagonal; else False.

    The algorithm works like this:

    Matrix with indices for reference:
    [[  0.   1.   2.   3.   4.   5.   6.   7.]
     [  8.   9.  10.  11.  12.  13.  14.  15.]
     [ 16.  17.  18.  19.  20.  21.  22.  23.]
     [ 24.  25.  26.  27.  28.  29.  30.  31.]
     [ 32.  33.  34.  35.  36.  37.  38.  39.]
     [ 40.  41.  42.  43.  44.  45.  46.  47.]
     [ 48.  49.  50.  51.  52.  53.  54.  55.]
     [ 56.  57.  58.  59.  60.  61.  62.  63.]]

    It checks right-to-left columns in 2 steps:
    * First, it checks each right-to-left diagonal that begins with each element on the first row
      (skipping the first index, since that "diagonal" is just element[0]) So the indices
      of each start of each row-based diagonal are: 1, 2, 3, 4, 5, 6, 7. In order to find the
      indices of each subsequent element in each diagonal, it adds (size-1) to the initial
      diagonal. For example: if we are checking the right-to-left diagonal starting with index 2,
      the diagonal should be indices: 2, 9, 16 (each is separated by 7). In order to perform
      this math, the nxn matrix is flattened.
    * Second, it does roughly the same thing for the right-to-left diagonals that start on the
      far-right column (indices 15, 23, 31, 39, 47, 55, 63). """

    size = len(board)
    flat = board.reshape((1, size*size))[0]
    # Check right-to-left diagonals
    for row_index in range(1, size):
        #print("row_index:", row_index)
        index = row_index
        diag_sum = 0
        for diag_index in range(row_index+1):
            #print("\tdiag_index: {0}, value: {1}".format(index, flat[index]))
            diag_sum += flat[index]
            index += (size - 1)
        if diag_sum > 1:
            return False

    col_diag_index = 0
    diag_lengths = list(range(size-1, 0, -1))
    for last_col_index in range(2*size-1, size*size-1, size):
        #print("col_index:", last_col_index)
        index = last_col_index
        diag_sum = 0
        diag_len = diag_lengths[col_diag_index]
        col_diag_index += 1
        for diag_index in range(diag_len):
            #print("\tdiag_index: {0}, value: {1}".format(index, flat[index]))
            diag_sum += flat[index]
            index += (size - 1)
        if diag_sum > 1:
            return False

    return True


def left_to_right_diagonals_valid(board):
    """ Returns True if there is no more than 1 "1" in each left-to-right diagonal; else False.

    To check the left-to-right diagonals, just rotate the matrix by 90 degrees and
    then use the right-to-left algorithm on the rotated matrix. """

    rotated_board = np.rot90(board)
    return right_to_left_diagonals_valid(rotated_board)


def diags_valid(board):
    """ Returns True if there are no more than 1 "1" in any diagonal; else False. """

    return right_to_left_diagonals_valid(board) and left_to_right_diagonals_valid(board)


def rows_valid(board):
    """ Returns True if there are no more than 1 "1" in any row; else False. """

    for row in board:
        if np.sum(row) > 1:
            return False
    return True


def cols_valid(board):
    """ Returns True if there are no more than 1 "1" in any column; else False. """

    for col_index in range(len(board)):
        if np.sum(board[:, col_index]) > 1:
            return False
    return True


def is_valid(board):
    """ Returns True if there are no more than 1 "1" in any row, column, or diagonal;
    Else, it returns False. """

    return rows_valid(board) and cols_valid(board) and diags_valid(board)


def n_queens(size):
    board = np.zeros((size, size))
    for row in range(size):
        for col in range(size):
            board[row][col] = size * row + col
    return board

if __name__ == '__main__':
    board_size = 8
    solution = n_queens(board_size)
    print(solution)
    print(diags_valid(solution))

