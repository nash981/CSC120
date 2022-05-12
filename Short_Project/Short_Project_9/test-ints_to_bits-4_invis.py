#! /usr/bin/python3

""" Code to test the ints_to_bits() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

ints = [179, 28, 163, 148, 19, 48, 220, 3, 42]



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

