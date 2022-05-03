#! /usr/bin/python3

""" Code to test the codes_to_chunks() function

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

msg = """'Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.

\"Beware the Jabberwock, my son!
      The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
      The frumious Bandersnatch!\"

He took his vorpal sword in hand;
      Long time the manxome foe he sought -
So rested he by the Tumtum tree
      And stood awhile in thought.

And, as in uffish thought he stood,
      The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
      And burbled as it came!

One, two! One, two! And through and through
      The vorpal blade went snicker-snack!
He left it dead, and with its head
      He went galumphing back.

\"And hast thou slain the Jabberwock?
      Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!\"
      He chortled in his joy.

'Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.

  -- Lewis Carroll"""



# MAP
mapping = {'m': "000000",
           '"': "000001000",
           'p': "000001001",
           'v': "00000101",
           'c': "0000011",
           'w': "000010",
           'O': "000011000",
           'B': "000011001",
           'C': "00001101",
           '!': "0000111",
           'e': "0001",
           'u': "001000",
           'g': "001001",
           's': "00101",
           'i': "00110",
           'f': "0011100",
           '.': "00111010",
           "'": "0011101100",
           'x': "0011101101",
           'L': "001110111",
           'A': "0011110",
           'j': "00111110",
           'J': "00111111",
           'n': "01000",
           'r': "01001",
           '\n': "01010",
           'y': "010110",
           'H': "01011100",
           'S': "0101110100",
           "<END>": "0101110101",
           'D': "010111011",
           '?': "0101111000",
           ';': "0101111001",
           ':': "010111101",
           '-': "01011111",
           'l': "01100",
           'd': "01101",
           't': "0111",
           ' ': "10",
           ',': "110000",
           'k': "1100010",
           'T': "1100011",
           'b': "11001",
           'h': "1101",
           'a': "1110",
           'o': "1111",
          }



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing codes_to_chunks()...")
    print()

    print(f"INPUT MESSAGE: {repr(msg)}")
    print()

    print("MAPPING:")
    for c in mapping:
        print(f"  {repr(c)}   {mapping[c]}")
    print()

    codes  = huffman_tools.str_to_codes(msg, mapping)
    retval = huffman_tools.codes_to_chunks(codes)

    print("Returned chunks:")
    for chunk in retval:
        print(f"          \"{repr(chunk)[1:-1]}\",")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

