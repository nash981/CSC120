#! /usr/bin/python3

""" Code to test the ints_to_bits() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

ints = [86, 221, 39, 131, 255, 182, 9, 248, 246, 69, 183, 112, 106, 35, 227, 160, 191, 228, 39, 108]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing ints_to_bits()...")
    print()

    print(f"INPUT INTEGERS: {ints}")
    print()

    retval = huffman_tools.ints_to_bits(ints)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

