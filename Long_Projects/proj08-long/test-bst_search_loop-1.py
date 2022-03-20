#! /usr/bin/python3

""" Code to test the bst_search_loop() function

    Author: Russ Lewis
"""

import tree_funcs_long



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)

root.left  = TreeNode(-31)
root.right = TreeNode(52)

root.left.left  = TreeNode(-50)
root.left.right = TreeNode(-25)

root.right.left  = TreeNode(12)
root.right.right = TreeNode(66)

root.right.left.left  = TreeNode(-17)
root.right.left.right = TreeNode(50)

root.right.left.left.right = TreeNode(4)

root.right.left.left.right.left  = TreeNode(-6)
root.right.left.left.right.right = TreeNode(9)

root.right.left.right.left = TreeNode(40)

root.right.left.left.right = TreeNode(-12)

root.right.left.right.left  = TreeNode(34)

root.right.left.right.left.left = TreeNode(26)

root.right.left.right.left.left.left = TreeNode(25)

root.right.right.right = TreeNode(81)

root.right.right.right.left  = TreeNode(77)
root.right.right.right.right = TreeNode(83)

root.right.right.right.left.right = TreeNode(80)

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

    test_one(-19)
    test_one(0)
    test_one(83)
    test_one(12)
    test_one(17)
    test_one(12)
    test_one(34)
    test_one(1234)
    test_one(-1234)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


