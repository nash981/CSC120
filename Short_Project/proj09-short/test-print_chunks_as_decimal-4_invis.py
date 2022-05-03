#! /usr/bin/python3

""" Code to test the print_chunks_as_decimal() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

chunks = ["11111111",
          "11111010",
          "11110001",
          "01011111",
          "10011100",
          "01111000",
          "01011001",
          "01011000",
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

