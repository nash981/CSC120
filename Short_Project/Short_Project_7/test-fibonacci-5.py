#! /usr/bin/python3

""" Code to test the annoying_fibonacci() function

    Author: Russ Lewis
"""

import annoying_recursion_short





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 5

    print("Testing annoying_fibonacci()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion_short.annoying_fibonacci(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


