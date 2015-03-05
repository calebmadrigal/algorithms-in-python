""" Prefix calculator. Takes a space-delimited string like '* ( / 10 5 ) ( + ( - 5 2 ) ( * 1 3 ) )'
and parses it, builds an AST, and reduces the AST to a number by running specified operators. """

__author__ = "Caleb Madrigal"
__date__ = "2015-03-04"


def calc(node):
    if node == ():
        return
    (op, a, b) = node[0], node[1], node[2]
    if type(a) == tuple:
        a = calc(a)
    if type(b) == tuple:
        b = calc(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def build_ast(token_list):
    if not token_list:
        return (), ()
    token, *rest = token_list
    if token == '(':
        internal, remainder = build_ast(rest)
        internal2, remainder2 = build_ast(remainder)
        return (internal,) + internal2, remainder2
    elif token == ')':
        return (), rest
    elif token in ['+', '-', '*', '/']:
        internal, remainder = build_ast(rest)
        return (token,) + internal, remainder
    else:  # Token is number
        internal, remainder = build_ast(rest)
        return (float(token),) + internal, remainder


def parse(calc_str):
    return calc_str.split()

if __name__ == '__main__':
    calc_str = '+ ( * 2 2 ) ( - ( + 3 2 ) 4 )'
    parsed = parse(calc_str)
    ast, _ = build_ast(parsed)
    print("Original: '{}'".format(calc_str))
    print("Parsed:", parsed)
    print("AST:", ast)
    print("Result:", calc(ast))

    calc_str2 = '* ( / 10 5 ) ( + ( - 5 2 ) ( * 1 3 ) )'
    ast, _ = build_ast(parse(calc_str2))
    print("\nOriginal: '{}'".format(calc_str2))
    print("AST:", ast)
    print("Result:", calc(ast))

