from collections import OrderedDict


def restore_binary_tree(inorder, preorder):
    if not inorder:
        return None

    root = preorder[0]
    root_index_in_inorder = find_index_in_inorder(root, inorder)  # can be turned into a one-liner
    left_tree_size = root_index_in_inorder

    # This copies the array :(. Not linear!!
    left_inorder = inorder[:left_tree_size]
    left_preorder = preorder[1:left_tree_size + 1]
    left_tree = restore_binary_tree(left_inorder, left_preorder)

    right_inorder = inorder[left_tree_size + 1:]
    right_preorder = preorder[left_tree_size + 1:]
    right_tree = restore_binary_tree(right_inorder, right_preorder)

    # this is an artifact of automatic testing
    return OrderedDict([('value', root), ("left", left_tree), ("right", right_tree)])


def find_index_in_inorder(value, inorder):
    return next(i for i, v in enumerate(inorder) if v == value)
