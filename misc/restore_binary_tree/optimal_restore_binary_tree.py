from collections import OrderedDict


def restore_binary_tree(inorder, preorder):
    inorder_indices = {v: i for i, v in enumerate(inorder)}
    full_size = len(inorder)
    return restore_binary_tree_recursive(inorder, 0, full_size, preorder, 0, full_size, inorder_indices)


def restore_binary_tree_recursive(inorder, in_start, in_stop, preorder, pre_start, pre_stop, inorder_indices):
    if in_stop - in_start == 0:
        return None

    root = preorder[pre_start]
    left_len = inorder_indices[root] - in_start

    left_in_start = in_start
    left_in_stop = left_in_start + left_len
    left_pre_start = pre_start + 1
    left_pre_stop = left_pre_start + left_len
    left_tree = restore_binary_tree_recursive(
        inorder, left_in_start, left_in_stop, preorder, left_pre_start, left_pre_stop, inorder_indices)

    right_in_start = inorder_indices[root] + 1
    right_in_stop = in_stop
    right_pre_start = pre_start + left_len + 1
    right_pre_stop = pre_stop
    right_tree = restore_binary_tree_recursive(
        inorder, right_in_start, right_in_stop, preorder, right_pre_start, right_pre_stop, inorder_indices)

    return OrderedDict([('value', root), ("left", left_tree), ("right", right_tree)])