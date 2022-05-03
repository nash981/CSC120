#! /usr/bin/python3

""" Code to test the bits_to_str() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

bits = "00100100100101100100100100011111111111111111000011000000"

# MAP (AS A TREE)
root                         = TreeNode(None)

root.left                    = TreeNode(None)
root.right                   = TreeNode(None)

root.left .left              = TreeNode(None)
root.left .right             = ' '
root.right.left              = TreeNode(None)
root.right.right             = TreeNode(None)

root.left .left .left        = TreeNode(None)
root.left .left .right       = 's'
root.right.left .left        = 't'
root.right.left .right       = 'i'
root.right.right.left        = TreeNode(None)
root.right.right.right       = TreeNode(None)

root.left .left .left .left  = TreeNode(None)
root.left .left .left .right = TreeNode(None)
root.right.right.left .left  = TreeNode(None)
root.right.right.left .right = 'h'
root.right.right.right.left  = 'e'
root.right.right.right.right = 'a'

root.left .left .left .left .left  = 'T'
root.left .left .left .left .right = TreeNode(None)
root.left .left .left .right.left  = '.'
root.left .left .left .right.right = 'y'
root.right.right.left .left .left  = 'o'
root.right.right.left .left .right = 'n'

root.left .left .left .left .right.left  = 'l'
root.left .left .left .left .right.right = "<END>"



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bits_to_str()...")
    print()

    print(f"INPUT BITS: {bits}")
    print()

    retval = huffman_tools.bits_to_str(bits, root)

    print(f"Returned value: {repr(retval)}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

