#! /usr/bin/python3

""" Code to test the str_to_codes() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

msg = "This is a test.  This is only a test."

# MAP
mapping = {'T': "00000",
           'l': "000010",
           "<END>": "000011",
           '.': "00010",
           'y': "00011",
           's': "001",
           ' ': "01",
           't': "100",
           'i': "101",
           'o': "11000",
           'n': "11001",
           'h': "1101",
           'e': "1110",
           'a': "1111"
          }



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing str_to_codes()...")
    print()

    print(f"INPUT MESSAGE: {repr(msg)}")
    print()

    print("MAPPING:")
    for c in mapping:
        print(f"  {repr(c)}   {mapping[c]}")
    print()

    retval = huffman_tools.str_to_codes(msg, mapping)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


