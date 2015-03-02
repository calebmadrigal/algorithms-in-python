""" Binary Search Tree implemented with embedded lists. 

Node format: [value, left child, right child].
Leaf nodes look like: [value, [], []].
"""

__author__ = "Caleb Madrigal"
__date__ = "2015-02-25"


def node_value(node, new_value=None):
    """ Set value: node_value(node, value); Get value: node_value(node). """

    if new_value is not None:
        node[0] = new_value
    return node[0]


def left_child(node, new_node=None):
    """ Set left child: left_child(node, new_left_child); Get left node: left_child(node). """

    if new_node is not None:
        node[1] = new_node
    return node[1]


def right_child(node, new_node=None):
    """ Set right child: right_child(node, new_right_child); Get right node: right_child(node). """

    if new_node is not None:
        node[2] = new_node
    return node[2]


def add(tree, value):
    """ Adds value to tree and returns tree. """

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


def _find_node(tree, value, parent=None, is_right_child=False):
    """ Returns (node, parent, is_right_child_of_parent) if found (parent is None if root).
    If not found, return (None, None, False). """

    if tree == []:
        return (None, parent, is_right_child)
    if node_value(tree) == value:
        return (tree, parent, is_right_child)
    elif value < node_value(tree):
        return _find_node(left_child(tree), value, tree, False)
    else:  # value > node_value(tree)
        return _find_node(right_child(tree), value, tree, True)


def contains(tree, value):
    """ Returns true if value in tree; False otherwise. """

    return _find_node(tree, value)[0] != None


def _find_min_node(tree, parent=None, is_right_child=False):
    """ Finds the minimum node in a tree, and returns (node, parent, is_right_child),
    where node is the node with the minimum value, parent is the parent of the minimum
    node, and is_right_child is true if the minimum node is the right-child of its parent
    (or false if it is the left-child of its parent). """

    if left_child(tree) == []:
        return (tree, parent, is_right_child)
    else:
        return _find_min_node(left_child(tree), tree, False)


def _remove_node(node_to_remove, parent, is_right_child_of_parent):
    # If node not found, return
    if not node_to_remove:
        return

    def set_parent_reference(new_reference):
        if parent:
            if is_right_child_of_parent:
                right_child(parent, new_reference)
            else:
                left_child(parent, new_reference)

    # If the node to be removed has 2 children; Steps:
    #   * Set the node_to_remove value to the min value in the right subtree
    #   * call _remove_node() on the item which was swapped with
    if left_child(node_to_remove) != [] and right_child(node_to_remove) != []:
        (right_child_min_node, rchild_min_node_parent, is_min_right_child) = \
                _find_min_node(right_child(node_to_remove), node_to_remove, True)
        node_value(node_to_remove, node_value(right_child_min_node))
        _remove_node(right_child_min_node, rchild_min_node_parent, is_min_right_child)

    # If the node to be removed has just 1 child (the left child), set the parent reference
    # to the left child of the node to be removed
    elif left_child(node_to_remove) != []:
        set_parent_reference(left_child(node_to_remove))

    # If the node to be removed has just 1 child (the right child), set the parent reference
    # to the right child of the node to be removed
    elif right_child(node_to_remove) != []:
        set_parent_reference(right_child(node_to_remove))

    # The node has no children, so just remove it
    else:
        set_parent_reference([])


def remove(tree, value):
    (node_to_remove, parent, is_right_child_of_parent) = _find_node(tree, value)
    _remove_node(node_to_remove, parent, is_right_child_of_parent)


def inorder(tree):
    if tree == [] or node_value(tree) == None:
        return []
    return inorder(left_child(tree)) + [node_value(tree)] + inorder(right_child(tree))


def inorder_traverse(tree, visit_func):
    if tree == [] or node_value(tree) == None:
        return
    inorder_traverse(left_child(tree), visit_func)
    visit_func(node_value(tree))
    inorder_traverse(right_child(tree), visit_func)


def postorder_traverse(tree, visit_func):
    if tree == [] or node_value(tree) == None:
        return
    postorder_traverse(left_child(tree), visit_func)
    postorder_traverse(right_child(tree), visit_func)
    visit_func(node_value(tree))


def preorder_traverse(tree, visit_func):
    if tree == [] or node_value(tree) == None:
        return
    visit_func(node_value(tree))
    preorder_traverse(left_child(tree), visit_func)
    preorder_traverse(right_child(tree), visit_func)


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
    print("Tree:")
    print_tree(tree)
    print(tree)
    print("Is 5 in tree?", contains(tree, 5))
    print("Is 20 in tree?", contains(tree, 20))
    print("Is 100 in tree?", contains(tree, 100))
    print("Inorder:", inorder(tree))
    print("Inorder traversal: ", end="")
    inorder_traverse(tree, lambda node: print(node, end=", "))
    print("\nPostorder traversal: ", end="")
    postorder_traverse(tree, lambda node: print(node, end=", "))
    print("\nPreorder traversal: ", end="")
    preorder_traverse(tree, lambda node: print(node, end=", "))
    print()

    remove(tree, 8)
    print("Tree after removing 8:")
    print_tree(tree)
    print("Inorder:", inorder(tree))
