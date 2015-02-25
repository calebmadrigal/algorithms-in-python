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
    elif value < node_value(tree):
        left_child(tree, add(left_child(tree), value))
    elif value > node_value(tree):
        right_child(tree, add(right_child(tree), value))
    # If value == node_value(tree): It's already there - don't reinsert it
    return tree


def remove(tree, value):
    pass


def contains(tree, value):
    if tree == []:
        return False
    if node_value(tree) == value:
        return True
    return contains(left_child(tree), value) or contains(right_child(tree), value)


def inorder(tree):
    if tree == [] or node_value(tree) == None:
        return []
    return inorder(left_child(tree)) + [node_value(tree)] + inorder(right_child(tree))


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
    print("Is 5 in tree?", contains(tree, 5))
    print("Is 20 in tree?", contains(tree, 20))
    print("Is 100 in tree?", contains(tree, 100))
    print("Inorder:", inorder(tree))

