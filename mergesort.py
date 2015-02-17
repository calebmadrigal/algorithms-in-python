"""mergesort.py - implementation of mergesort. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-13"


def merge(left, right):
    if len(left) < 1:
        return right
    elif len(right) < 1:
        return left
    else:
        first_left, *rest_left = left
        first_right, *rest_right = right
        if first_left <= first_right:
            return [first_left] + merge(rest_left, right)
        else:
            return [first_right] + merge(left, rest_right)


def mergesort(lst):
    list_len = len(lst)
    if list_len < 2:
        return lst
    if list_len == 2:
        if lst[0] <= lst[1]:
            return lst
        else:
            return [lst[1], lst[0]]
    else: # list_len > 2
        split_point = list_len // 2
        left = lst[0:split_point]
        right = lst[split_point:]
        left_sorted = mergesort(left)
        right_sorted = mergesort(right)
        return merge(left_sorted, right_sorted)


if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*mergesort*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

