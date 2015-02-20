""" Various combinatorics functions. """

__author__ = "Caleb Madriagl"
__date__ = "2015-02-20"


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def permutations(lst):
    result = []

    def permute(current, rest):
        if rest == []:
            result.append(current)
            return

        for r in rest:
            permute(current + (r,), [i for i in rest if i != r])

    permute((), lst)
    return result


def subsets(lst):
    result = []

    def _subsets(current, rest):
        if rest == []:
            result.append(current)
            return

        (first, *rest) = rest
        _subsets(current + (first,), rest)
        _subsets(current, rest)

    _subsets((), lst)
    return result


if __name__ == "__main__":
    print("Permutations of ['a','b','c']:", permutations(['a','b','c']))
    print("Subsets of ['a','b','c']:", subsets(['a','b','c']))

