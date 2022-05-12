#! /usr/bin/python3

""" Code to test the annoying_factorial() function

    Author: Russ Lewis
"""

import annoying_recursion_short





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 8

    print("Testing annoying_factorial()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion_short.annoying_factorial(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


