#! /usr/bin/python3

""" Code to test the wordle utils word_filter() function

    Author: Russ Lewis
"""

import wordle_utils


dictionary_name = "words_05_noDupLetters.txt"

correct = "BUILT"
guesses = ["WHICH", "LOCUS", "FAULT", "SMART", "GUILT"]


###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    words = set()
    with open(dictionary_name) as f:
        for line in f:
            line = line.strip()
            if line != "":
                words.add(line)
    assert correct in words

    print("Testing word_filter()...")
    print()

    print(f"CORRECT: {correct}")
    print()
    print(f"STARTED WITH {len(words)} WORDS:")
    print()

    for g in guesses:
        match,miss = wordle_utils.check(g, correct)

        print(f"GUESS: {g}")
        print(f"       {match}")
        print(f"       {miss}")

        words = wordle_utils.word_filter(match,miss, words)
        print(f"{len(words)} words remain.")
        print()

    print("AFTER ALL GUESSES, THE FOLLOWING WORDS REMAIN:")
    for w in sorted(words):
        print(w)



if __name__ == "__main__":
    main()


