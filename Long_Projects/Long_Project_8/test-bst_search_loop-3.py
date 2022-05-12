#! /usr/bin/python3

""" Code to test the bst_search_loop() function

    Author: Russ Lewis
"""

import tree_funcs_long



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(8)

root.left = TreeNode(-27)

root.left.left = TreeNode(-47)
root.left.right = TreeNode(-15)

root.left.left.right = TreeNode(-33)
root.left.left.right.right = TreeNode(-30)

root.left.right.left = TreeNode(-16)

root.left.right.left.left = TreeNode(-25)

root.left.right.right = TreeNode(5)

root.left.right.right.left = TreeNode(-7)

root.left.right.right.left.right = TreeNode(4)

root.right = TreeNode(41)

root.right.left = TreeNode(21)
root.right.right = TreeNode(79)

root.right.left.left  = TreeNode(14)
root.right.left.right = TreeNode(24)

root.right.left.right.right = TreeNode(31)

root.right.right = TreeNode(54)
root.right.right.right = TreeNode(64)
root.right.right.right.right = TreeNode(85)
root.right.right.right.right.right = TreeNode(97)

#vals = tree_funcs_long.in_order_vals(root)
#print(vals)
#print(sorted(vals))
#assert sorted(vals) == vals



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bst_search_loop()...")
    print()

    def test_one(val):
        print(f"Testing with search key = {val}")
        retval = tree_funcs_long.bst_search_loop(root, val)
        if retval is None:
            print("    Returned: None")
        else:
            print(f"    Returned: val = {retval.val}")
        print()

    test_one(-7)
    test_one(0)
    test_one(83)
    test_one(32)
    test_one(31)
    test_one(12)
    test_one(-33)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


