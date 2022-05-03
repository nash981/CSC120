#! /usr/bin/python3

""" Code to test the codes_to_chunks() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

codes = ["00000", "1101", "101", "001", "01", "101", "001", "01", "1111",
         "01", "100", "1110", "001", "100", "00010", "01", "01", "00000",
         "1101", "101", "001", "01", "101", "001", "01", "11000", "11001",
         "000010", "00011", "01", "1111", "01", "100", "1110", "001", "100",
         "00010", "000011"]



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

