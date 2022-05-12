#! /usr/bin/python3

""" Code to test the wordle utils check() function

    Author: Russ Lewis
"""

import wordle_utils



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    guess   = "SONIC"
    compare = "SONIC"

    print("Testing the wordle utils check() function...")
    print()

    print(f"Correct: {compare}")
    print(f"Guess:   {guess}")
    print( "-----    " + "-"*len(guess))

    match,miss = wordle_utils.check(guess,compare)

    print(f"MATCH:   {match}")
    print(f"MISS:    {miss}")
    print()

    print()
    print("--------------- reversed ---------------")
    guess,compare = compare,guess
    print()

    print(f"Correct: {compare}")
    print(f"Guess:   {guess}")
    print( "-----    " + "-"*len(guess))

    match,miss = wordle_utils.check(guess,compare)

    print(f"MATCH:   {match}")
    print(f"MISS:    {miss}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


