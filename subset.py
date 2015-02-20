
def _print_subset(current, rest):
    if rest == []:
        print(current)
        return
    
    (first, *rest) = rest
    subset(current + [first], rest)
    subset(current, rest)


def print_subset(lst):
    subset([], lst)

if __name__ == '__main__':
    lst = [i for i in 'abcde']
    print(print_subset(lst))

