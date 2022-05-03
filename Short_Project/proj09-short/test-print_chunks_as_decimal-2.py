#! /usr/bin/python3

""" Code to test the print_chunks_as_decimal() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

chunks = ["11011010",
          "11010110",
          "11101000",
          "00000011",
          "01110111",
          "01010101",
          "01010101",
          "01000000",
         ]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing print_chunks_as_decimal()...")
    print()

    print("CHUNKS:")
    for ch in chunks:
        print(f"  {repr(ch)}")
    print()

    retval = huffman_tools.print_chunks_as_decimal(chunks)
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

