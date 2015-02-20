""" Backtracking solution to N-Queens problem. """

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
    * Step 1: it checks each right-to-left diagonal that begins with each element on the first row
      (skipping the first index, since that "diagonal" is just element[0]) So the indices
      of each start of each row-based diagonal are: 1, 2, 3, 4, 5, 6, 7. In order to find the
      indices of each subsequent element in each diagonal, it adds (size-1) to the initial
      diagonal. For example: if we are checking the right-to-left diagonal starting with index 2,
      the diagonal should be indices: 2, 9, 16 (each is separated by 7). In order to perform
      this math, the nxn matrix is flattened.
    * Step 2: it does roughly the same thing for the right-to-left diagonals that start on the
      far-right column (indices 15, 23, 31, 39, 47, 55, 63). """

    size = len(board)
    flat = board.reshape((1, size*size))[0]

    for row_index in range(1, size):
        index = row_index
        diag_sum = 0
        for diag_index in range(row_index+1):
            diag_sum += flat[index]
            index += (size - 1)
        if diag_sum > 1:
            return False

    col_diag_index = 0
    diag_lengths = list(range(size-1, 0, -1))
    for last_col_index in range(2*size-1, size*size-1, size):
        index = last_col_index
        diag_sum = 0
        diag_len = diag_lengths[col_diag_index]
        col_diag_index += 1
        for diag_index in range(diag_len):
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


def print_board_indented(board, row):
    print('\t'*row + str(board).replace('\n', '\n'+('\t'*row)))


def search(board, row=0, cols_taken=()):
    """ In-place search for solution to n-queens. Backtracking algorithm. """

    # Return if we are at the maximum depth and the solution is valid
    if row == len(board) and diags_valid(board):
        return True

    # Otherwise, try each column and recursively work down the rows
    for col in range(len(board)):
        if col in cols_taken:
            continue

        board[row][col] = 1
        print_board_indented(board, row)

        if diags_valid(board):
            if search(board, row+1, cols_taken + (col,)):
                return True
            else:
                board[row][col] = 0
        else:
            board[row][col] = 0

    return False


def n_queens(size):
    board = np.zeros((size, size))
    if search(board):
        print("Solution found:")
        print(board)
    else:
        print("No solution found")

if __name__ == '__main__':
    board_size = 8
    n_queens(board_size)

