""" Binary Search Tree implemented with embedded lists. """

__author__ = "Caleb Madrigal"
__date__ = "2015-02-25"


def node_value(node, new_value=None):
    if new_value:
        node[0] = new_value
    return node[0]


def left_child(node, new_node=None):
    if new_node:
        node[1] = new_node
    return node[1]


def right_child(node, new_node=None):
    if new_node:
        node[2] = new_node
    return node[2]


def add(tree, value):
    if tree == []:
        tree = [value, [], []]
    elif node_value(tree) == None:
        node_value(tree, value)
    elif value <= node_value(tree):
        left_child(tree, add(left_child(tree), value))
    else:
        right_child(tree, add(right_child(tree), value))
    return tree


def remove(tree, value):
    pass


def is_in(tree, value):
    pass


def print_tree(tree, indent=0):
    if tree == [] or node_value(tree) == None:
        return
    print('\t'*indent + str(node_value(tree)))
    print_tree(left_child(tree), indent+1)
    print_tree(right_child(tree), indent+1)


if __name__ == '__main__':
    tree = []
    for i in [5, 3, 8, 5, 2, 10, 20, 15, 30, 0, 7]:
        tree = add(tree, i)
    print_tree(tree)

