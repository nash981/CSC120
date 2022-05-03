"""
Author: Nishant Athawale
Date: 5th April 2022
Assignment: Long Project 10: Bob
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: This program aims to print all the palindromes in the set of
            words present in a given text file and their combinations
            upto a given word length.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


def set_builder(filename):
    """
    This function filters all the non-alphabetical characters
    and builds the set of all words found in the given text file.
    If the given file is not found, then the function prints an error
    message and terminates the program.
    Parameters:
        filename: Name of the file that is to be processed.
    Returns
        outset: Set of all the unique words in the given text file.
    """
    try:
        text = open(filename, "r")
        out_set = set()
        for line in text:
            out_str = ""
            for i in range(len(line)):
                if line[i].isalpha() is True:
                    out_str += line[i]
                elif line[i] == "-" or line[i] == "'":
                    out_str += ""
                else:
                    out_str += " "
            word_list = out_str.strip().split()
            for words in word_list:
                if len(words) >= 2:
                    out_set.add(words.lower())
        return out_set
    except FileNotFoundError:
        print(f"ERROR: Could not open the input file: {filename}")
        exit()


def check_palindrome(word):
    """
    This function checks whether the given the word is a palindrom or not.
    Paramters:
        word: The word which is to be checked if it is a palindrome or not.
    Returns:
        True: If the given word is palindrome
        False: If the given word is not palindrome
    """
    for i in range(int(len(word)/2)):
        if word[i] != word[-i-1]:
            return False
    return True


def one_word_palin_check(word_set):
    """
    This function checks if any words in the given set of words have
    are palindromes.
    Parameters:
        word_set: The set of unique words found in the given txt file.
    Returns:
        one_word_palindrome: set of one word palindromes
    """
    one_word_palindrome = []
    for words in word_set:
        if check_palindrome(words) is True:
            one_word_palindrome.append(words)
    return one_word_palindrome


def two_three_word_palin_check(word_set):
    """
    This function checks if combinations of any two and three words
    in the given set of words have are palindromes.
    Parameters:
        word_set: The set of unique words found in the given txt file.
    Returns:
        two_three_word_palindrome: set of two and three word combination
         palindromes.
   """
    two_three_word_palindrome = []
    for words in word_set:
        for words2 in word_set:
            if check_palindrome(words+words2) is True:
                two_three_word_palindrome.append(words+words2)
            for words3 in word_set:
                if check_palindrome(words+words2+words3) is True:
                    two_three_word_palindrome.append(words + words2 + words3)
    return set(two_three_word_palindrome)


def length_based_dict_builder(word_set):
    """
    This function builds a dictionary maps a length key to a list
    of words having the same length.
    Parameters:
        word_set: The set of unique words found in the given txt file.
    Returns:
        main_dict: Dictionary maps a length key to a list of words
        having the same length.
    """
    main_dict = {}
    for words in word_set:
        if len(words) not in main_dict.keys():
            main_dict[len(words)] = set()
        main_dict[len(words)].add(words)
    return main_dict


def general_palindrome_check(length_based_dict, n, word_set):
    """
    This function checks length wise whether words of different lengths
    are palindromes or not.
        If the word is a palindrome, then it adds to the word list mapped
        to its length key in a separate dictionary
        If the word is not a palindrome, then the function updated the given
        dictionary with combination of the given word with all the words in
        the original word set that are not palindromes.
        This process repeats until the loop reaches the user specified length.
    Parameters:
        length_based_dict: Dictionary maps a length key to a list of words
        having the same length.
        n: The user specified length
        word_set: The set of unique words found in the given txt file.
    Returns:
        palin_dict: The dictionary mapping the list of palindromes of same
        length to the length as the keys.
    """
    palin_dict = {}
    for i in range(n):
        if i+1 not in palin_dict.keys():
            palin_dict[i+1] = set()
        if i+1 not in length_based_dict.keys():
            length_based_dict[i+1] = set()
        else:
            for words in length_based_dict[i+1]:
                if check_palindrome(words) is True:
                    palin_dict[i+1].add(words)
                else:
                    for word2 in word_set:
                        if check_palindrome(word2) is False:
                            new_word = words+word2
                            if len(new_word) not in length_based_dict.keys():
                                length_based_dict[len(new_word)] = set()
                            length_based_dict[len(new_word)].add(new_word)
    return palin_dict


def output_print(length_based_dict, palin_dict, n, one_w_palins, \
                 two_three_w_palins):
    """
    This function prints the output in the desired format.
    Parameters:
        length_based_dict: Dictionary maps a length key to a list of words
        having the same length.
        palin_dict: The dictionary mapping the list of palindromes of same
        length to the length as the keys.
        n: The user specified length
        one_w_palins: set of one word palindromes
        two_three_w_palins: set of two and three word combination
        palindromes.
    Returns: None
    """
    print("1-WORD PALINDROMES:")
    for words in sorted(one_w_palins):
        print(f"  {words}")
    print("\n2-WORD AND 3-WORD PALINDROMES:")
    for words2 in sorted(two_three_w_palins):
        print(f"  {words2}")
    for i in range(n):
        print(f"\nPALINDROMES OF LENGTH {i+1}    - " +
              f"length of candidate list: {len(length_based_dict[i+1])}")
        for palindromes in sorted(palin_dict[i+1]):
            print(f"  {palindromes}")


def main():
    """
    The main accepts input and executes the program.
    """
    filename = input()
    n = input()
    word_set = set_builder(filename)
    if n.lower() == "dump":
        print("WORD LIST:")
        for words in sorted(word_set):
            print(f"  {words}")
    else:
        one_w_palindromes = one_word_palin_check(word_set)
        two_three_w_palindromes = two_three_word_palin_check(word_set)
        length_based_dict = length_based_dict_builder(word_set)
        palin_dict = general_palindrome_check(length_based_dict, \
                                              int(n), word_set)
        output_print(length_based_dict, palin_dict, int(n), \
                     one_w_palindromes, two_three_w_palindromes)


if __name__ == '__main__':
    main()
