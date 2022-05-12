from tree_node import *


def tree_count(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    elif root.left is not None and root.right is None:
        return 1 + tree_count(root.left)
    elif root.left is None and root.right is not None:
        return 1 + tree_count(root.right)
    elif root.left is not None and root.right is not None:
        return 1 + tree_count(root.left) + tree_count(root.right)


def tree_sum(root):
    if root is None:
        return 0
    elif root.left is not None and root.right is not None:
        return root.val + tree_sum(root.left) + tree_sum(root.right)
    elif root.left is not None and root.right is None:
        return root.val + tree_sum(root.left)
    elif root.left is None and root.right is not None:
        return root.val + tree_sum(root.right)
    elif root.left is None and root.right is None:
        return root.val


def tree_depth(root):
    if root is None:
        return -1
    elif root.left is None and root.right is None:
        return 0
    elif root.left is not None and root.right is None:
        return 1 + tree_depth(root.left)
    elif root.left is None and root.right is not None:
        return 1 + tree_depth(root.right)
    elif root.left is not None and root.right is not None:
        left_depth = tree_depth(root.left)
        right_depth = tree_depth(root.right)
        if left_depth > right_depth:
            return 1 + left_depth
        else:
            return 1 + right_depth


def tree_print(root):
    if root is None:
        print()
    elif root.left is None and root.right is None:
        print(root.val)
    elif root.left is not None and root.right is None:
        print(root.val)
        tree_print(root.left)
    elif root.left is None and root.right is not None:
        print(root.val)
        tree_print(root.right)
    elif root.left is not None and root.right is not None:
        print(root.val)
        tree_print(root.left)
        tree_print(root.right)


def tree_build_left_linked_list(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
        root = TreeNode(data[0])
        return root
    else:
        root = TreeNode(data[0])
        root.left = tree_build_left_linked_list(data[1:])
        return root

