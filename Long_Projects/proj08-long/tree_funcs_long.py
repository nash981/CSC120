"""
Author: Nishant Athawale
Date: 22nd March 2022
Assignment: Long Project 8: Trees
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: In this assignment, I develop different functions
            to do the following:
            1. Find the maximum value in a tree
            2. Find the maximum value in a Binary Search Tree
            6. Find a given value in a tree
            7. Find a given value in a Binary Search Tree
            9. Insert a value in a Binary Search Tree
            3. Pre-Order traversal of the tree
            4. In-Order traversal of the tree
            5. Post-Order traversal of the tree
            8. Return the values of the tree as an array in the order of
               in-order traversal
            Note: For the purpose of this assignment, all trees used are
            binary trees.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""
from tree_node import *


def tree_max(root):
    """
    This take the root node of the tree as a parameter and recursively
    finds the maximum value in the Binary Tree.

    Parameters:
        root: Root Node of the binary
    Returns:
        The maximum value among the root value, maximum value of the
        right subtree and maximum value of the left subtree.
    """
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
    """
    This take the root node of the tree as a parameter and recursively
    finds the maximum value in the Binary Search Tree by recursively
    accessing and returning the right most leaf node.
    Parameters:
        root: Root Node of the binary
    Returns:
        The value of the right most leaf node in the subsequent
        subtree.
    """
    if root.right is None:
        return root.val
    else:
        return bst_max(root.right)


def bst_search_loop(root, val):
    """
    This function searches for a given value in the given binary search
    tree and returns the node containing that value. This function finds
    the value by using loops.
    Parameters:
        root: Root Node of the binary
        val: Desired value to be searched
    Return:
        If value found: The node containing the desired value
        If value not found: None
    """
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
    """
    This function recursively searches for a given value in the given
    binary tree and returns the node containing that value.
    Parameters:
        root: Root Node of the binary
        val: Desired value to be searched
    Returns:
        If value found: The node containing the desired value
        If value not found: None
    """
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
    """
    This function inserts a given value in a given binary
    search tree. It finds the node of insertion by using recursion.
    Parameters:
        root: Root Node of the binary
        val: Desired value to be searched
    Returns: None
    """
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
    """
    This function prints a given tree by using pre order
    traversal
    Parameters:
        root: Root Node of the binary
    Returns:
        None
    """
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
    """
    This function prints a given tree by using in order
    traversal
    Parameters:
        root: Root Node of the binary
    Returns:
        None
    """
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
    """
    This function prints a given tree by using post order
    traversal
    Parameters:
        root: Root Node of the binary
    Returns:
        None
    """
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
    """
    This function returns an array of the values stored in a tree
    ordered in the way of in-order traversal.
    Parameters:
        root: Root Node of the binary
    Returns:
        An array of the values stored in the array.
    """
    val = []
    if root is not None:
        if root.left is None and root.right is None:
            return [root.val]
        elif root.left is not None and root.right is None:
            val += in_order_vals(root.left) + [root.val]
        elif root.left is None and root.right is not None:
            val += [root.val] + in_order_vals(root.right)
        elif root.left is not None and root.right is not None:
            val += in_order_vals(root.left) + [root.val] + \
                   in_order_vals(root.right)
    return val
