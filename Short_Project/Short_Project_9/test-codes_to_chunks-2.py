#! /usr/bin/python3

""" Code to test the codes_to_chunks() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

codes = ["1101101011",
         "010110",
         "11101",
         "000000",
         "0001101",
         "1101110",
         "10101010101",
         "010101",
        ]



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

