#! /usr/bin/python3

""" Code to test a Huffman encoding process.  This does everything
    except to generate the mapping, which is hard-coded.

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

ints = [90,89,74,112,163,245,168,112,36,124,52,90,86,173,117,195,177,35,213,102,242,15,41,45,12,57,190,166,2,46,69,131,152,143,98,236,60,93,18,61,138,209,126,186,78,145,166,81,116,81,164,49,30,223,141,90,234,215,101,208,65,174,158,74,47,229,164,224,232,116,167,36,178,83,250,236,143,52,145,237,248,132,214,88,72,246,40,215,216,198,43,110,210,89,123,22,29,22,145,54,241,96,185,132,212,148,225,106,81,116,75,20,28,15,188,69,200,44,97,3,236,12,147,123,69,146,81,161,26,152,11,74,87,135,222,29,241,136,126,225,3,44,36,123,28,29,67,94,195,79,37,209,40,184,30,67,102,251,6,82,7,212,192,66,234,67,140,32,2,85,32,83,144,83,123,13,60,218,252,203,49,5,180,148,30,108,90,69,65,138,12,165,100,148,95,199,139,201,203,55,134,48,189,72,150,148,152,121,175,23,68,143,99,7,230,18,131,200,235,21,194,234,67,141,141,41,69,129,91,248,43,35,216,176,142,145,167,146,210,147,166,15,123,189,100,123,29,59,224,173,101,209,35,216,203,13,60,131,93,84,34,172,71,152,77,89,156,17,65,192,82,72,44,97,253,122,71,38,49,91,118,48,251,193,250,236,186,37,192,242,223,21,131,32,66,242,66,234,67,139,41,75,229,94,40,117,100,84,24,167,67,165,54,12,213,150,178,22,82,136,114,92,41,34,228,123,24,64,4,170,64,181,145,115,16,107,202,68,25,105,73,161,53,96,204,114,184,248,22,32,207,230,183,150,4,160,198,216,106,209,100,5,252,49,105,73,210,131,129,237,5,76,4,92,178,149,24,135,148,60,122,160,227,207,14,40,191,145,236,186,32,8,31,129,153,115,15,228,210,3,79,38,164,254,129,189,36,92,208,154,178,179,72,129,249,49,151,93,104,73,30,197,208,65,174,158,74,15,255,174,23,148,212,192,69,200,245,89,69,192,242,27,55,217,104,28,178,148,71,156,8,56,108,133,191,46,210,29,83,129,106,12,83,95,144,28,146,46,90,77,69,14,148,212,192,80,165,148,162,19,124,98,29,169,69,63,153,57,38,132,25,101,40,219,129,7,9,23,93,150,111,19,67,24,135,157,74,196,123,26,150,2,0,61,148,89,41,253,118,66,107,32,181,76,5,57,84,179,126,73,71,222,34,61,86,97,83,33,129,174,156,177,199,36,178,133,224,195,219,200,185,182,89,83,1,30,196,61,154,121,33,80,243,128,36,38,240,102,166,192,248,52,137,104,52,141,144,183,227,82,184,246,40,80,134,55,176,114,166,2,46,83,172,125,195,26,18,21,15,56,2,66,111,143,239,96,229,76,4,92,166,174,221,75,49,30,196,61,154,121,45,41,93,52,178,147,142,69,28,128,217,4,24,206,129,198,152,105,230,49,143,156,120,194,222,53,172,167,67,249,6,28,146,19,120,50,8,1,47,56,186,36,123,68,184,78,2,146,98,96,230,33,55,159,97,237,228,121,164,171,9,30,198,88,105,228,216,30,178,150,96,101,165,36,123,23,30,222,66,112,20,146,200,33,161,21,194,111,62,195,219,200,243,73,86,19,66,97,223,87,192,203,74,72,246,33,55,148,26,45,25,117,214,132,232,255,84,28,60,93,18,61,136,92,234,198,23,132,5,48,211,201,11,126,40,58,159,242,77,169,150,107,6,101,196,166,172,126,129,0,57,43,193,167,123,41,65,139,172,222,71,177,15,102,158,65,144,64,9,83,160,202,160,248,201,53,36,123,27,112,7,183,201,133,188,75,162,104,99,21,183,107,203,218,153,102,178,131,205,141,8,3,146,88,195,144,1,84,222,90,82,97,112,183,162,2,141,72,239,214,49,136,118,165,16,228,224,136,243,9,30,171,94,164,119,235,18,19,89,183,139,115,132,71,177,65,128,188,93,18,61,136,77,241,138,217,205,143,233,128,123,72,51,14,248,112,128,195,129,150,148,175,131,161,210,146,61,86,106,71,126,177,33,53,145,236,92,20,119,32,37,23,242,23,82,28,71,177,169,176,62,13,35,100,39,1,73,63,165,36,123,46,30,205,60,156,179,73,4,24,132,222,12,133,212,172,71,177,91,186,205,243,22,145,40,41,170,44,147,46,126,160,225,34,229,46,98,127,196,121,164,139,175,250,199,233,1,35,216,142,255,161,127,166,81,210,166,248,52,90,68,186,38,134,49,15,245,15,111,48,183,136,99,131,168,114,3,146,81,127,35,216,132,222,184,246,49,52,19,66,2,113,127,35,216,164,15,97,167,146,23,82,28,104,79,53,150,87,230,72,98,194,45,83,147,24,135,250,135,183,174,210,52,133,66,195,146,71,152,72,246,40,48,23,139,162,71,177,65,229,21,82,2,98,168,56,74,25,175,16,168,120,191,156,179,73,5,145,127,196,123,46,131,202,42,164,4,208,222,82,38,249,192,82,74,25,175,70,43,76,200,113,83,184,115,36,162,254,90,78,107,173,228,126,128,138,30,6,90,82,88,254,176,20,43,171,93,148,64,148,180,90,69,148,90,82,90,197,192,148,212,193,24,199,206,60,127,50,72,246,54,209,99,31,80,37,98,210,147,15,176,98,46,71,177,182,139,46,183,116,131,45,41,57,144,227,82,177,195,154,204,122,172,181,36,180,13,83,98,71,177,113,237,241,140,114,38,38,12,111,104,141,143,180,193,136,243,9,105,12,188,90,77,243,128,164,148,183,226,46,90,195,133,140,116,11,18,183,116,173,118,90,238,172,90,80,198,164,133,245,48,84,192,71,181,121,5,249,146,81,247,136,143,101,236,44,194,93,18,227,219,204,90,86,187,40,178,26,193,144,64,9,86,18,5,152,232,9,131,25,113,6,71,152,72,88,130,198,92,76,116,4,193,147,24,173,187,47,15,176,109,246,93,18,9,199,138,14,2,146,101,196,130,197,166,194,223,147,24,173,185,132,186,38,117,15,111,60,214,65,109,37,166,194,223,146,81,1,74,13,25,117,214,221,136,118,168,170,14,16,199,154,204,122,172,184,82,97,3,225,123,215,24,199,1,227,226,4,139,145,236,66,127,82,72,44,131,1,120,186,37,209,71,77,235,90,162,139,250,244,38,32,44,76,236,155,32,177,30,97,46,138,58,111,89,65,226,192,200,32,4,132,248,139,145,230,19,19,73,4,24,133,207,17,30,197,209,71,77,229,208,120,176,244,104,224,199,40,144,177,190,101,40,216,16,194,247,136,243,9,14,226,223,72,52,155,83,44,222,24,213,151,156,93,18,60,247,139,162,142,155,214,184,93,72,112,51,82,71,177,135,221,101,39,74,24,186,37,110,233,6,98,2,196,206,201,178,131,197,129,144,64,9,11,169,14,6,121,150,84,192,80,121,26,144,50,87,30,247,2,14,49,234,178,208,194,245,35,146,70,162,192,204,123,25,112,136,84,165,89,23,63,162,117,152,25,105,73,30,97,49,236,96,165,154,200,185,4,227,203,135,239,227,197,165,36,62,220,1,226,61,86,71,127,208,37,98,19,121,107,35,216,132,248,164,12,69,200,243,222,32,131,16,185,226,35,216,186,40,233,188,186,13,22,6,111,153,74,33,98,154,180,55,201,30,223,170,75,72,98,157,11,120,129,248,163,239,17,30,123,197,52,178,167,22,17,250,4,0,235,33,117,33,203,143,98,11,42,178,205,246,106,75,21,82,202,152,10,221,210,89,65,48,107,45,104,125,2,196,92,199,170,37,169,43,73,229,42,12,82,228,44,121,225,192,215,71,122,205,34,160,197,46,66,198,31,96,192,200,243,9,30,171,49,84,28,33,141,160,224,124,24,186,36,38,243,19,6,55,14,201,165,6,48,181,217,96,152,52,101,195,235,8,51,72,149,187,164,133,74,85,145,230,19,66,80,121,26,144,49,2,70,148,89,74,35,216,133,153,67,198,26,86,73,4,24,143,98,9,229,55,19,74,215,107,136,78,120,9,79,228,150,148,148,105,17,12,67,102,251,46,137,2,127,7,200,20,57,36,94,148,111,153,74,32,177,176,36,56,12,180,164,129,35,74,57,102,240,203,167,222,18,232,144,74,119,73,79,176,82,66,161,226,61,138,154,248,223,50,148,65,99,11,82,72,32,197,165,199,183,148,251,5,36,42,30,35,217,123,9,253,32,203,89,9,172,219,82,72,247,236,71,156,11,105,73,13,155,236,180,14,12,219,155,26,82,141,9,136,11,18,11,27,106,73,142,7,178,241,208,19,6,139,72,217,116,72,246,43,70,254,146,223,136,248,24,180,164,253,65,195,156,11,44,161,120,48,246,248,209,194,235,135,148,60,98,101,82,24,139,132,222,147,47,56,25,10,135,138,28,223,66,24,162,254,89,74,6,66,161,226,141,124,83,174,205,73,30,199,234,14,18,214,186,221,210,96,165,154,200,22,69,205,236,71,177,250,131,132,25,86,18,5,155,31,165,152,188,145,114,141,77,95,17,236,66,127,14,16,177,111,198,164,26,226,228,21,74,72,16,145,236,101,134,158,86,187,33,56,18,155,6,69,202,13,248,162,254,122,162,33,115,155,230,82,143,50,204,65,63,206,35,216,130,97,21,101,218,82,81,127,61,86,66,164,184,69,165,39,170,203,252,60,210,12,139,148,185,101,40,133,212,135,24,152,49,100,58,178,204,90,82,80,237,245,124,89,120,232,22,37,165,37,77,99,83,1,135,50,24,180,79,48,23,3,239,41,102,178,210,146,21,15,22,82,140,176,211,205,198,90,112]



from tree_node import TreeNode

root                                                                         = TreeNode(None)
root.left                                                                    = TreeNode(None)
root.left .left                                                              = TreeNode(None)
root.left .left .left                                                        = TreeNode(None)
root.left .left .left .left                                                  = TreeNode(None)
root.left .left .left .left .left                                            = TreeNode(None)
root.left .left .left .left .left .left                                      = 'u'
root.left .left .left .left .left .right                                     = TreeNode(None)
root.left .left .left .left .left .right.left                                = 'b'
root.left .left .left .left .left .right.right                               = ','
root.left .left .left .left .right                                           = TreeNode(None)
root.left .left .left .left .right.left                                      = 'w'
root.left .left .left .left .right.right                                     = TreeNode(None)
root.left .left .left .left .right.right.left                                = 'y'
root.left .left .left .left .right.right.right                               = TreeNode(None)
root.left .left .left .left .right.right.right.left                          = TreeNode(None)
root.left .left .left .left .right.right.right.left .left                    = 'k'
root.left .left .left .left .right.right.right.left .right                   = TreeNode(None)
root.left .left .left .left .right.right.right.left .right.left              = 'x'
root.left .left .left .left .right.right.right.left .right.right             = 'A'
root.left .left .left .left .right.right.right.right                         = TreeNode(None)
root.left .left .left .left .right.right.right.right.left                    = TreeNode(None)
root.left .left .left .left .right.right.right.right.left .left              = 'W'
root.left .left .left .left .right.right.right.right.left .right             = 'U'
root.left .left .left .left .right.right.right.right.right                   = TreeNode(None)
root.left .left .left .left .right.right.right.right.right.left              = TreeNode(None)
root.left .left .left .left .right.right.right.right.right.left .left        = TreeNode(None)
root.left .left .left .left .right.right.right.right.right.left .left .left  = 'z'
root.left .left .left .left .right.right.right.right.right.left .left .right = 'q'
root.left .left .left .left .right.right.right.right.right.left .right       = TreeNode(None)
root.left .left .left .left .right.right.right.right.right.left .right.left  = 'Y'
root.left .left .left .left .right.right.right.right.right.left .right.right = 'S'
root.left .left .left .left .right.right.right.right.right.right             = 'N'
root.left .left .left .right                                                 = 't'
root.left .left .right                                                       = ' '
root.left .right                                                             = TreeNode(None)
root.left .right.left                                                        = TreeNode(None)
root.left .right.left .left                                                  = TreeNode(None)
root.left .right.left .left .left                                            = TreeNode(None)
root.left .right.left .left .left .left                                      = 'c'
root.left .right.left .left .left .right                                     = 'f'
root.left .right.left .left .right                                           = 'd'
root.left .right.left .right                                                 = TreeNode(None)
root.left .right.left .right.left                                            = 'l'
root.left .right.left .right.right                                           = TreeNode(None)
root.left .right.left .right.right.left                                      = TreeNode(None)
root.left .right.left .right.right.left .left                                = 'v'
root.left .right.left .right.right.left .right                               = TreeNode(None)
root.left .right.left .right.right.left .right.left                          = TreeNode(None)
root.left .right.left .right.right.left .right.left .left                    = TreeNode(None)
root.left .right.left .right.right.left .right.left .left .left              = TreeNode(None)
root.left .right.left .right.right.left .right.left .left .left .left        = 'O'
root.left .right.left .right.right.left .right.left .left .left .right       = TreeNode(None)
root.left .right.left .right.right.left .right.left .left .left .right.left  = 'P'
root.left .right.left .right.right.left .right.left .left .left .right.right = 'L'
root.left .right.left .right.right.left .right.left .left .right             = TreeNode(None)
root.left .right.left .right.right.left .right.left .left .right.left        = 'F'
root.left .right.left .right.right.left .right.left .left .right.right       = TreeNode(None)
root.left .right.left .right.right.left .right.left .left .right.right.left  = 'E'
root.left .right.left .right.right.left .right.left .left .right.right.right = '<END>'
root.left .right.left .right.right.left .right.left .right                   = TreeNode(None)
root.left .right.left .right.right.left .right.left .right.left              = TreeNode(None)
root.left .right.left .right.right.left .right.left .right.left .left        = TreeNode(None)
root.left .right.left .right.right.left .right.left .right.left .left .left  = 'C'
root.left .right.left .right.right.left .right.left .right.left .left .right = '?'
root.left .right.left .right.right.left .right.left .right.left .right       = TreeNode(None)
root.left .right.left .right.right.left .right.left .right.left .right.left  = ';'
root.left .right.left .right.right.left .right.left .right.left .right.right = ':'
root.left .right.left .right.right.left .right.left .right.right             = "'"
root.left .right.left .right.right.left .right.right                         = TreeNode(None)
root.left .right.left .right.right.left .right.right.left                    = 'T'
root.left .right.left .right.right.left .right.right.right                   = 'G'
root.left .right.left .right.right.right                                     = '\n'
root.left .right.right                                                       = TreeNode(None)
root.left .right.right.left                                                  = 'a'
root.left .right.right.right                                                 = 'o'
root.right                                                                   = TreeNode(None)
root.right.left                                                              = TreeNode(None)
root.right.left .left                                                        = TreeNode(None)
root.right.left .left .left                                                  = TreeNode(None)
root.right.left .left .left .left                                            = TreeNode(None)
root.right.left .left .left .left .left                                      = 'g'
root.right.left .left .left .left .right                                     = 'p'
root.right.left .left .left .right                                           = TreeNode(None)
root.right.left .left .left .right.left                                      = 'm'
root.right.left .left .left .right.right                                     = TreeNode(None)
root.right.left .left .left .right.right.left                                = '.'
root.right.left .left .left .right.right.right                               = TreeNode(None)
root.right.left .left .left .right.right.right.left                          = TreeNode(None)
root.right.left .left .left .right.right.right.left .left                    = TreeNode(None)
root.right.left .left .left .right.right.right.left .left .left              = '"'
root.right.left .left .left .right.right.right.left .left .right             = 'I'
root.right.left .left .left .right.right.right.left .right                   = 'j'
root.right.left .left .left .right.right.right.right                         = TreeNode(None)
root.right.left .left .left .right.right.right.right.left                    = 'H'
root.right.left .left .left .right.right.right.right.right                   = TreeNode(None)
root.right.left .left .left .right.right.right.right.right.left              = 'B'
root.right.left .left .left .right.right.right.right.right.right             = '-'
root.right.left .left .right                                                 = 'n'
root.right.left .right                                                       = TreeNode(None)
root.right.left .right.left                                                  = 'i'
root.right.left .right.right                                                 = 's'
root.right.right                                                             = TreeNode(None)
root.right.right.left                                                        = 'e'
root.right.right.right                                                       = TreeNode(None)
root.right.right.right.left                                                  = 'h'
root.right.right.right.right                                                 = 'r'



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    bits = huffman_tools.ints_to_bits(ints)
    text = huffman_tools.bits_to_str (bits, root)

    print("UNCOMPRESSED MESSAGE:")
    print(text)
    print()

    print(f"COMPRESSED LENGTH  : {len(ints)}")
    print(f"UNCOMPRESSED LENGTH: {len(text)}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

