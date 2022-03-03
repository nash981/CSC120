#! /usr/bin/python3

""" Code to test the annoying_parens() function

    Author: Russ Lewis
"""

import annoying_recursion_short





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 0

    print("Testing annoying_parens()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion_short.annoying_parens(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


