""" Reverse function recursively and iteratively. """


def reverse(lst):
    if lst == []:
        return lst
    else:
        return reverse(lst[1:]) + [lst[0]]


def reverse_iter(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-1*(i+1)] = lst[-1*(i+1)], lst[i]
    return lst


if __name__ == '__main__':
    print(reverse(range(10)))
    print(reverse_iter(range(10)))

