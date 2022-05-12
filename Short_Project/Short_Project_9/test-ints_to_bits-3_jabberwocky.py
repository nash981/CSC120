#! /usr/bin/python3

""" Code to test the ints_to_bits() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

ints = [59,49,133,197,178,147,49,134,39,11,144,217,244,98,176,207,171,79,224,162,85,85,82,236,205,137,89,35,114,27,18,96,50,193,140,137,244,96,187,34,189,81,230,50,0,192,21,104,33,72,207,163,103,211,228,248,40,151,5,85,81,228,54,125,24,15,0,100,243,233,111,33,201,79,100,78,148,160,64,100,66,228,140,250,49,255,103,34,144,188,30,44,32,22,139,232,14,170,170,199,163,31,112,69,159,121,236,153,199,9,244,96,108,224,139,62,243,192,249,193,232,117,6,68,46,72,207,163,31,145,147,226,51,100,201,110,23,33,177,116,132,42,170,177,232,199,18,64,6,242,11,6,121,13,20,149,28,224,244,56,33,74,92,25,255,241,90,98,192,190,144,79,50,40,94,150,198,69,188,134,175,42,170,163,191,160,153,204,0,207,163,1,200,59,124,1,142,120,218,49,124,130,117,229,245,46,159,36,74,226,219,70,202,211,232,216,200,1,200,2,116,136,170,170,143,33,177,95,253,183,5,166,96,198,68,251,228,19,174,116,165,30,67,112,184,177,145,16,112,225,139,179,239,144,78,189,163,21,255,219,130,170,171,30,140,127,217,200,164,47,7,139,8,35,62,194,176,150,243,145,198,112,3,130,131,120,1,130,211,28,56,195,32,153,245,62,65,59,62,140,228,48,145,90,11,253,184,42,170,143,33,182,72,78,88,45,184,177,158,7,192,8,117,40,48,129,194,112,188,60,24,64,225,56,94,30,60,134,207,169,242,9,219,144,217,245,62,65,58,170,170,199,163,2,250,65,60,203,44,230,140,16,161,226,160,192,241,10,87,202,142,7,136,58,151,6,96,156,120,207,52,121,184,92,134,193,25,246,51,150,209,230,170,170,151,6,8,80,241,60,194,0,4,233,144,77,158,7,136,233,74,4,30,67,109,226,188,251,228,69,103,25,19,232,199,253,156,138,66,240,120,151,133,85,80,111,128,51,252,2,215,36,2,225,0,181,145,224,12,93,179,235,7,80,98,56,158,201,247,144,89,188,176,120,55,152,207,253,15,6,243,25,203,7,4,42,170,151,6,7,190,151,96,182,50,45,49,99,239,88,233,74,59,49,133,197,178,147,49,134,39,11,144,217,244,98,176,207,171,79,224,162,85,85,82,236,205,137,89,35,114,27,18,96,50,193,140,137,244,96,187,34,189,81,230,50,0,192,21,104,33,72,207,163,103,211,228,248,40,151,5,85,81,228,54,125,24,15,0,100,243,233,111,33,201,79,100,78,148,170,95,95,142,226,17,139,6,242,83,236,98,234]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing ints_to_bits()...")
    print()

    print(f"INPUT INTEGERS: {ints}")
    print()

    retval = huffman_tools.ints_to_bits(ints)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()
