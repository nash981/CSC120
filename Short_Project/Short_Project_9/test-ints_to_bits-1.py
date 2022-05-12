#! /usr/bin/python3

""" Code to test the ints_to_bits() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

ints = [6,210,210,251,56,193,40,54,150,151,25,8,111,179,140,16,96]



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

