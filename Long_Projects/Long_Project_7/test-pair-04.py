#! /usr/bin/python3

""" Code to test the pair_recursive() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_recursion_long



# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals1  = []
vals2  = [-11, -3, 79, 19, 72, 21, 70, -4, -5, -35, 39, 79, 46, -6, -47, -24, 80, 45]
nodes1 = [list_node.ListNode(val) for val in vals1]
nodes2 = [list_node.ListNode(val) for val in vals2]

in_list1 = None

in_list2 = nodes2[0]
for i in range(len(vals2)-1):
    nodes2[i].next = nodes2[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing pair_recursive()...")
    print()
    print(f"Input list 1: {in_list1}")
    print(f"Input list 2: {in_list2}")
    print()

    out_list = linked_list_recursion_long.pair_recursive(in_list1, in_list2)

    print(f"Output list: {out_list}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


