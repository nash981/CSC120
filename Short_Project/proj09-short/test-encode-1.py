#! /usr/bin/python3

""" Code to test a Huffman encoding process.  This does everything
    except to generate the mapping, which is hard-coded.

    Author: Russ Lewis
"""

import huffman_tools



###########################################################
#                       INPUT                             #
###########################################################

msg = """Fellow-Countrymen:

At this second appearing to take the oath of the Presidential office there is
less occasion for an extended address than there was at the first. Then a
statement somewhat in detail of a course to be pursued seemed fitting and
proper. Now, at the expiration of four years, during which public declarations
have been constantly called forth on every point and phase of the great contest
which still absorbs the attention and engrosses the energies of the nation,
little that is new could be presented. The progress of our arms, upon which all
else chiefly depends, is as well known to the public as to myself, and it is, I
trust, reasonably satisfactory and encouraging to all. With high hope for the
future, no prediction in regard to it is ventured.

On the occasion corresponding to this four years ago all thoughts were
anxiously directed to an impending civil war. All dreaded it, all sought to
avert it. While the inaugural address was being delivered from this place,
devoted altogether to saving the Union without war, insurgent agents were in
the city seeking to destroy it without war-seeking to dissolve the Union and
divide effects by negotiation. Both parties deprecated war, but one of them
would make war rather than let the nation survive, and the other would accept
war rather than let it perish, and the war came.

One-eighth of the whole population were colored slaves, not distributed
generally over the Union, but localized in the southern part of it. These
slaves constituted a peculiar and powerful interest. All knew that this
interest was somehow the cause of the war. To strengthen, perpetuate, and
extend this interest was the object for which the insurgents would rend the
Union even by war, while the Government claimed no right to do more than to
restrict the territorial enlargement of it. Neither party expected for the war
the magnitude or the duration which it has already attained. Neither
anticipated that the cause of the conflict might cease with or even before the
conflict itself should cease. Each looked for an easier triumph, and a result
less fundamental and astounding. Both read the same Bible and pray to the same
God, and each invokes His aid against the other. It may seem strange that any
men should dare to ask a just God's assistance in wringing their bread from the
sweat of other men's faces, but let us judge not, that we be not judged. The
prayers of both could not be answered. That of neither has been answered fully.

The Almighty has His own purposes. "Woe unto the world because of offenses; for
it must needs be that offenses come, but woe to that man by whom the offense
cometh." If we shall suppose that American slavery is one of those offenses
which, in the providence of God, must needs come, but which, having continued
through His appointed time, He now wills to remove, and that He gives to both
North and South this terrible war as the woe due to those by whom the offense
came, shall we discern therein any departure from those divine attributes which
the believers in a living God always ascribe to Him? Fondly do we hope,
fervently do we pray, that this mighty scourge of war may speedily pass away.
Yet, if God wills that it continue until all the wealth piled by the bondsman's
two hundred and fifty years of unrequited toil shall be sunk, and until every
drop of blood drawn with the lash shall be paid by another drawn with the
sword, as was said three thousand years ago, so still it must be said "the
judgements of the Lord are true and righteous altogether."

With malice toward none, with charity for all, with firmness in the right as
God gives us to see the right, let us strive on to finish the work we are in,
to bind up the nation's wounds, to care for him who shall have borne the battle
and for his widow and his orphan, to do all which may achieve and cherish a
just and lasting peace among ourselves and with all nations."""



mapping = {'u': '000000',
           'b': '0000010',
           ',': '0000011',
           'w': '000010',
           'y': '0000110',
           'k': '000011100',
           'x': '0000111010',
           'A': '0000111011',
           'W': '0000111100',
           'U': '0000111101',
           'z': '000011111000',
           'q': '000011111001',
           'Y': '000011111010',
           'S': '000011111011',
           'N': '0000111111',
           't': '0001',
           ' ': '001',
           'c': '010000',
           'f': '010001',
           'd': '01001',
           'l': '01010',
           'v': '0101100',
           'O': '01011010000',
           'P': '010110100010',
           'L': '010110100011',
           'F': '01011010010',
           'E': '010110100110',
           '<END>': '010110100111',
           'C': '010110101000',
           '?': '010110101001',
           ';': '010110101010',
           ':': '010110101011',
           "'": '0101101011',
           'T': '010110110',
           'G': '010110111',
           '\n': '010111',
           'a': '0110',
           'o': '0111',
           'g': '100000',
           'p': '100001',
           'm': '100010',
           '.': '1000110',
           '"': '1000111000',
           'I': '1000111001',
           'j': '100011101',
           'H': '100011110',
           'B': '1000111110',
           '-': '1000111111',
           'n': '1001',
           'i': '1010',
           's': '1011',
           'e': '110',
           'h': '1110',
           'r': '1111'
          }



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    codes  = huffman_tools.str_to_codes(msg, mapping)
    chunks = huffman_tools.codes_to_chunks(codes)
    huffman_tools.print_chunks_as_decimal(chunks)
    print()

    print(f"INPUT LENGTH:      {len(msg)}")
    print(f"COMPRESSED LENGTH: {len(chunks)}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

