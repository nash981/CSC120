#! /usr/bin/python3

""" Code to test the bits_to_str() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

bits = "001110110011000110000101110001011011001010010011001100011000011000100111000010111001000011011001111101000110001010110000110011111010101101001111111000001010001001010101010101010101001011101100110011011000100101011001001000110111001000011011000100100110000000110010110000011000110010001001111101000110000010111011001000101011110101010001111001100011001000000000110000000001010101101000001000010100100011001111101000110110011111010011111001001111100000101000100101110000010101010101010100011110010000110110011111010001100000001111000000000110010011110011111010010110111100100001110010010100111101100100010011101001010010100000010000000110010001000010111001001000110011111010001100011111111101100111001000101001000010111100000111100010110000100000000101101000101111101000000011101010101010101010110001111010001100011111011100000100010110011111011110011110110010011001110001110000100111110100011000000110110011100000100010110011111011110011110000001111100111000001111010000111010100000110010001000010111001001000110011111010001100011111100100011001001111100010001100110110010011001001011011100001011100100001101100010111010010000100001010101010101010110001111010001100011100010010010000000000011011110010000010110000011001111001000011010001010010010101000111001110000011110100001110000010000101001010010111000001100111111111111100010101101001100010110000001011111010010000010011110011001000101000010111101001011011000110010001011011110010000110101011110010101010101010101000111011111110100000100110011100110000000000110011111010001100000001110010000011101101111100000000011000111001111000110110100011000101111100100000100111010111100101111101010010111010011111001001000100101011100010110110110100011011001010110100111110100011011000110010000000000111001000000000100111010010001000101010101010101010001111001000011011000101011111111111011011011100000101101001100110000011000110010001001111101111100100000100111010111001110100101001010001111001000011011100001011100010110001100100010001000001110000111000011000101110110011111011111001000001001110101111011010001100010101111111111101101110000010101010101010101100011110100011000111111111011001110010001010010000101111000001111000101100001000001000110011111011000010101100001001011011110011100100011100011001110000000000111000001010000011011110000000000110000010110100110001110000111000110000110010000010011001111101010011111001000001001110110011111010001100111001000011000010010001010110100000101111111101101110000010101010101010100011110010000110110110010010000100111001011000001011011011100010110001100111100000011111000000000010000111010100101000001100001000000111000010011100001011110000111100000110000100000011100001001110000101111000011110001111001000011011001111101010011111001000001001110110111001000011011001111101010011111001000001001110101010101010101010110001111010001100000010111110100100000100111100110010110010110011100110100011000001000010100001111000101010000011000000111100010000101001010111110010101000111000000111100010000011101010010111000001100110000010011100011110001100111100110100011110011011100001011100100001101100000100011001111101100011001110010110110100011110011010101010101010101001011100000110000010000101000011110001001111001100001000000000000001001110100110010000010011011001111000000111100010001110100101001010000001000001111001000011011011011110001010111100111110111110010001000101011001110001100100010011111010001100011111111101100111001000101001000010111100000111100010010111100001010101010101010000011011111000000000110011111111000000001011010111001001000000001011100001000000001011010110010001111000000000110001011101101100111110101100000111010100000110001000111000100111101100100111110111100100000101100110111100101100000111100000110111100110001100111111111101000011110000011011110011000110011100101100000111000001000010101010101010100101110000011000000111101111101001011101100000101101100011001000101101001100010110001111101111010110001110100101001010001110110011000110000101110001011011001010010011001100011000011000100111000010111001000011011001111101000110001010110000110011111010101101001111111000001010001001010101010101010101001011101100110011011000100101011001001000110111001000011011000100100110000000110010110000011000110010001001111101000110000010111011001000101011110101010001111001100011001000000000110000000001010101101000001000010100100011001111101000110110011111010011111001001111100000101000100101110000010101010101010100011110010000110110011111010001100000001111000000000110010011110011111010010110111100100001110010010100111101100100010011101001010010101010010111110101111110001110111000100001000110001011000001101111001001010011111011000110001011101010"

root                                                             = TreeNode(None)
root.left                                                        = TreeNode(None)
root.left .left                                                  = TreeNode(None)
root.left .left .left                                            = TreeNode(None)
root.left .left .left .left                                      = TreeNode(None)
root.left .left .left .left .left                                = TreeNode(None)
root.left .left .left .left .left .left                          = 'm'
root.left .left .left .left .left .right                         = TreeNode(None)
root.left .left .left .left .left .right.left                    = TreeNode(None)
root.left .left .left .left .left .right.left .left              = TreeNode(None)
root.left .left .left .left .left .right.left .left .left        = '"'
root.left .left .left .left .left .right.left .left .right       = 'p'
root.left .left .left .left .left .right.left .right             = 'v'
root.left .left .left .left .left .right.right                   = 'c'
root.left .left .left .left .right                               = TreeNode(None)
root.left .left .left .left .right.left                          = 'w'
root.left .left .left .left .right.right                         = TreeNode(None)
root.left .left .left .left .right.right.left                    = TreeNode(None)
root.left .left .left .left .right.right.left .left              = TreeNode(None)
root.left .left .left .left .right.right.left .left .left        = 'O'
root.left .left .left .left .right.right.left .left .right       = 'B'
root.left .left .left .left .right.right.left .right             = 'C'
root.left .left .left .left .right.right.right                   = '!'
root.left .left .left .right                                     = 'e'
root.left .left .right                                           = TreeNode(None)
root.left .left .right.left                                      = TreeNode(None)
root.left .left .right.left .left                                = TreeNode(None)
root.left .left .right.left .left .left                          = 'u'
root.left .left .right.left .left .right                         = 'g'
root.left .left .right.left .right                               = 's'
root.left .left .right.right                                     = TreeNode(None)
root.left .left .right.right.left                                = 'i'
root.left .left .right.right.right                               = TreeNode(None)
root.left .left .right.right.right.left                          = TreeNode(None)
root.left .left .right.right.right.left .left                    = 'f'
root.left .left .right.right.right.left .right                   = TreeNode(None)
root.left .left .right.right.right.left .right.left              = '.'
root.left .left .right.right.right.left .right.right             = TreeNode(None)
root.left .left .right.right.right.left .right.right.left        = TreeNode(None)
root.left .left .right.right.right.left .right.right.left .left  = "'"
root.left .left .right.right.right.left .right.right.left .right = 'x'
root.left .left .right.right.right.left .right.right.right       = 'L'
root.left .left .right.right.right.right                         = TreeNode(None)
root.left .left .right.right.right.right.left                    = 'A'
root.left .left .right.right.right.right.right                   = TreeNode(None)
root.left .left .right.right.right.right.right.left              = 'j'
root.left .left .right.right.right.right.right.right             = 'J'
root.left .right                                                 = TreeNode(None)
root.left .right.left                                            = TreeNode(None)
root.left .right.left .left                                      = TreeNode(None)
root.left .right.left .left .left                                = 'n'
root.left .right.left .left .right                               = 'r'
root.left .right.left .right                                     = TreeNode(None)
root.left .right.left .right.left                                = '\n'
root.left .right.left .right.right                               = TreeNode(None)
root.left .right.left .right.right.left                          = 'y'
root.left .right.left .right.right.right                         = TreeNode(None)
root.left .right.left .right.right.right.left                    = TreeNode(None)
root.left .right.left .right.right.right.left .left              = 'H'
root.left .right.left .right.right.right.left .right             = TreeNode(None)
root.left .right.left .right.right.right.left .right.left        = TreeNode(None)
root.left .right.left .right.right.right.left .right.left .left  = 'S'
root.left .right.left .right.right.right.left .right.left .right = '<END>'
root.left .right.left .right.right.right.left .right.right       = 'D'
root.left .right.left .right.right.right.right                   = TreeNode(None)
root.left .right.left .right.right.right.right.left              = TreeNode(None)
root.left .right.left .right.right.right.right.left .left        = TreeNode(None)
root.left .right.left .right.right.right.right.left .left .left  = '?'
root.left .right.left .right.right.right.right.left .left .right = ';'
root.left .right.left .right.right.right.right.left .right       = ':'
root.left .right.left .right.right.right.right.right             = '-'
root.left .right.right                                           = TreeNode(None)
root.left .right.right.left                                      = TreeNode(None)
root.left .right.right.left .left                                = 'l'
root.left .right.right.left .right                               = 'd'
root.left .right.right.right                                     = 't'
root.right                                                       = TreeNode(None)
root.right.left                                                  = ' '
root.right.right                                                 = TreeNode(None)
root.right.right.left                                            = TreeNode(None)
root.right.right.left .left                                      = TreeNode(None)
root.right.right.left .left .left                                = TreeNode(None)
root.right.right.left .left .left .left                          = ','
root.right.right.left .left .left .right                         = TreeNode(None)
root.right.right.left .left .left .right.left                    = 'k'
root.right.right.left .left .left .right.right                   = 'T'
root.right.right.left .left .right                               = 'b'
root.right.right.left .right                                     = 'h'
root.right.right.right                                           = TreeNode(None)
root.right.right.right.left                                      = 'a'
root.right.right.right.right                                     = 'o'


###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bits_to_str()...")
    print()

    print(f"INPUT BITS: {bits}")
    print()

    retval = huffman_tools.bits_to_str(bits, root)

    print(f"Returned value: {repr(retval)}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

