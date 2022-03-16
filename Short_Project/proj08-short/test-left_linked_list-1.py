#! /usr/bin/python3

""" Code to test the tree_build_left_linked_list() function

    Author: Russ Lewis
"""

import tree_funcs_short



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

vals = [ -19, 52, 12, 66, 50, -31, 81, -6, 77, 34, 26, -17, -12, 40, 80, 4, -25, 25, -50, 83, 9 ]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_build_left_linked_list()...")
    print()

    root = tree_funcs_short.tree_build_left_linked_list(vals)

    print("RETURNED TREE:")

    cur = root
    while cur is not None:
        print(f"There is a node with value {cur.val}")

        if cur.right is not None:
            print("ERROR: This node has a right node, that is wrong!!!")
        cur = cur.left

    print()
    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


