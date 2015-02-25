""" Fibonacci sequence. """


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_iter(n):
    n_minus_1 = 1
    n_minus_2 = 0
    current = 1
    for i in range(n):
        current = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = current

    return current


if __name__ == '__main__':
    print([fib(i) for i in range(10)])
    print([fib_iter(i) for i in range(10)])
    print(fib_iter(1000))

