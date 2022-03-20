from tree_node import *


def tree_max(root):
    if root.left is None and root.right is None:
        return root.val
    elif root.left is not None and root.right is None:
        max_apparent = tree_max(root.left)
        if max_apparent >= root.val:
            return max_apparent
        else:
            return root.val
    elif root.left is None and root.right is not None:
        max_apparent = tree_max(root.right)
        if max_apparent >= root.val:
            return max_apparent
        else:
            return root.val
    elif root.left is not None and root.right is not None:
        left_max = tree_max(root.left)
        right_max = tree_max(root.right)
        if left_max > right_max:
            if left_max > root.val:
                return left_max
            else:
                return root.val
        else:
            if right_max > root.val:
                return right_max
            else:
                return root.val


def bst_max(root):
    if root.right is None:
        return root.val
    else:
        return bst_max(root.right)


def bst_search_loop(root, val):
    curr = root
    if curr is not None:
        while curr.left is not None or curr.right is not None:
            if curr.val == val:
                return curr
            if curr.val > val:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr = curr.right
            elif curr.val < val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr = curr.left
        if curr.val == val:
            return curr
    return None


def tree_search(root, val):
    if root is None:
        return None
    elif root.val == val:
        return root
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is not None and root.right is None:
            return tree_search(root.left, val)
        elif root.left is None and root.right is not None:
            return tree_search(root.right, val)
        elif root.left is not None and root.right is not None:
            left = tree_search(root.left, val)
            right = tree_search(root.right, val)
            if left is not None:
                return left
            elif right is not None:
                return right
            else:
                return None


def bst_insert_loop(root, val):
    curr = root
    while True:
        if curr.val > val:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
        elif curr.val < val:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right


def pre_order_traversal_print(root):
    if root is None:
        return None
    else:
        print(root.val)
        if root.left is not None and root.right is None:
            pre_order_traversal_print(root.left)
        elif root.left is None and root.right is not None:
            pre_order_traversal_print(root.right)
        elif root.left is not None and root.right is not None:
            pre_order_traversal_print(root.left)
            pre_order_traversal_print(root.right)


def in_order_traversal_print(root):
    if root is None:
        return None
    else:
        if root.left is None and root.right is None:
            print(root.val)
        elif root.left is not None and root.right is None:
            in_order_traversal_print(root.left)
            print(root.val)
        elif root.left is None and root.right is not None:
            print(root.val)
            in_order_traversal_print(root.right)
        elif root.left is not None and root.right is not None:
            in_order_traversal_print(root.left)
            print(root.val)
            in_order_traversal_print(root.right)


def post_order_traversal_print(root):
    if root is None:
        return None
    else:
        if root.left is not None and root.right is None:
            post_order_traversal_print(root.left)
        elif root.left is None and root.right is not None:
            post_order_traversal_print(root.right)
        elif root.left is not None and root.right is not None:
            post_order_traversal_print(root.left)
            post_order_traversal_print(root.right)
        print(root.val)


def in_order_vals(root):
    val = []
    if root is not None:
        if root.left is None and root.right is None:
            return root.val
        elif root.left is not None and root.right is None:
            if type(in_order_vals(root.left)) is list:
                val += in_order_vals(root.left)
            else:
                val.append(in_order_vals(root.left))
            val.append(root.val)
        elif root.left is None and root.right is not None:
            val.append(root.val)
            if type(in_order_vals(root.right)) is list:
                val += in_order_vals(root.right)
            else:
                val.append(in_order_vals(root.right))
        elif root.left is not None and root.right is not None:
            if type(in_order_vals(root.left)) is list:
                val += in_order_vals(root.left)
            else:
                val.append(in_order_vals(root.left))
            val.append(root.val)
            if type(in_order_vals(root.right)) is list:
                val += in_order_vals(root.right)
            else:
                val.append(in_order_vals(root.right))
    return val
