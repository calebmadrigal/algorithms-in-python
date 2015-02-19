""" N-Queens solutions. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-19"

import numpy as np


def right_to_left_diagonals_valid(board):
    """ Returns True if there is no more than 1 queen in each diagonal, False otherwise.

    [[  0.   1.   2.   3.   4.   5.   6.   7.]
     [  8.   9.  10.  11.  12.  13.  14.  15.]
     [ 16.  17.  18.  19.  20.  21.  22.  23.]
     [ 24.  25.  26.  27.  28.  29.  30.  31.]
     [ 32.  33.  34.  35.  36.  37.  38.  39.]
     [ 40.  41.  42.  43.  44.  45.  46.  47.]
     [ 48.  49.  50.  51.  52.  53.  54.  55.]
     [ 56.  57.  58.  59.  60.  61.  62.  63.]]

    The algorithm works like this:

    TBD

    """

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

def diags_valid(board):
    if not right_to_left_diagonals_valid(board):
        return False
    rotated_board = np.rot90(board)
    return right_to_left_diagonals_valid(rotated_board)


def rows_valid(board):
    for row in board:
        if np.sum(row) > 1:
            return False
    return True


def cols_valid(board):
    for col_index in len(board):
        if np.sum(board[:,col_index]) > 1:
            return False
    return True


def is_valid(board):
    return rows_valid(board) and cols_valid(board) and diags_valid(board)


def n_queens(size):
    board = np.zeros((size, size))
    for row in range(size):
        for col in range(size):
            board[row][col] = size * row + col
    return board

if __name__ == '__main__':
    size = 8
    solution = n_queens(size)
    print(solution)
    print(diags_valid(solution))

