#! /usr/bin/python3

""" Code to test the annoying_very_quizzical() function

    Author: Russ Lewis
"""

import annoying_recursion_short





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 5

    print("Testing annoying_very_quizzical()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion_short.annoying_very_quizzical(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


