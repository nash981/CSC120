#! /usr/bin/python3

""" Code to test the tree_count() function

    Author: Russ Lewis
"""

import tree_funcs_short



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_print()...")
    print()

    tree_funcs_short.tree_print(root)

    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


