#! /usr/bin/python3

""" Code to test the is_rev_sorted_recursive() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_recursion_short





# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals  = [-38, 56, -1, -11, -47, 66, 21, 61, 19, 71, -2, -48, 57, 96, 68, -21, 95, -32, 67, 12][::-1]
nodes = [list_node.ListNode(val) for val in vals]

in_list = nodes[0]
for i in range(len(vals)-1):
    nodes[i].next = nodes[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing is_rev_sorted_recursive()...")
    print()
    print(f"Input list: {in_list}")

    retval = linked_list_recursion_short.is_rev_sorted_recursive(in_list)

    print(f"retval: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


