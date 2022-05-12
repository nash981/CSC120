#! /usr/bin/python3

""" Code to test the str_to_codes() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

msg = "abcdefabcdefabcdefabcdef"

# MAP
mapping = {'e': "000",
           'd': "001",
           'c': "010",
           'b': "011",
           'a': "100",
           "<END>": "101",
           'f': "11",
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


