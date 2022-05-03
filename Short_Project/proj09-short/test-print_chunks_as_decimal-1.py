#! /usr/bin/python3

""" Code to test the print_chunks_as_decimal() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

chunks = ["00000110",
          "11010010",
          "11010010",
          "11111011",
          "00111000",
          "11000001",
          "00101000",
          "00110110",
          "10010110",
          "10010111",
          "00011001",
          "00001000",
          "01101111",
          "10110011",
          "10001100",
          "00010000",
          "01100000",
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

