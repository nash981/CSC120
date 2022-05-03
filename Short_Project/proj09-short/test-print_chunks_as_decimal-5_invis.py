#! /usr/bin/python3

""" Code to test the print_chunks_as_decimal() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

chunks = ["01000010",
          "11001010",
          "11000110",
          "11011100",
          "11001001",
          "00001111",
          "10000000",
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

