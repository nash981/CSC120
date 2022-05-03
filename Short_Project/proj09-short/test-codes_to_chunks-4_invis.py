#! /usr/bin/python3

""" Code to test the codes_to_chunks() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

import random
random.seed(0xdeadbeef)

def gen_code():
    retval = ""
    for _ in range(random.randint(2,20)):
        if random.randint(0,1) == 0:
            retval += '0'
        else:
            retval += '1'
    return retval

codes = [ gen_code() for _ in range(random.randint(5,25)) ]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing codes_to_chunks()...")
    print()

    print(f"INPUT CODES:")
    for code in codes:
        print(f"  {repr(code)}")
    print()

    retval = huffman_tools.codes_to_chunks(codes)

    print("Returned chunks")
    for chunk in retval:
        print(f"  {repr(chunk)}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

