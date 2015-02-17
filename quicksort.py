"""quicksort.py - implementation of quicksort. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-14"


def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[-1]
        low = []
        high = []
        for i in lst[:-1]:
            if i <= pivot:
                low.append(i)
            else:
                high.append(i)
        return quicksort(low) + [pivot] + quicksort(high)

if __name__ == "__main__":
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*quicksort*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

