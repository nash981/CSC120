"""
Author: Nishant Athawale
Date: 22nd March 2022
Assignment: Long Project 8: Trees
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: This program aims to print all the words that rhyme with
            the words given as input by the user.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


def file_read(filename):
    """
    This function reads the given file and processes all lines into
    a list of words in all lines.
    Parameters:
        filename: Name of the file to be read
    Returns:
        word_list: List of all the words in the world
    """
    word_list = []
    txt = open(filename, "r")
    for lines in txt:
        word_list.append(lines.strip().split())
    txt.close()
    return word_list


def spell_to_pronunciation(word_list):
    """
    This functions builds a dictionary with the words as the keys
    and the list of their constituent phonemes as their respective
    value.
    Parameters:
        word_list: List of all the words in the world
    Returns:
        spell_dict: a dictionary with the words as the keys
                    and the list of their constituent phonemes
                    as their respective value.
    """
    spell_dict = {}
    for i in range(len(word_list)):
        word, phenoms = word_list[i][0], word_list[i][1:]
        if word in spell_dict:
            x = [spell_dict[word], phenoms]
            spell_dict[word] = x
        else:
            spell_dict[word] = phenoms
    return spell_dict


def primary_phenom_dict(word_list):
    """
    This functions builds a dictionary with the primary stresses as the keys
    and the list of all the words containing the primary stresses as their
    respective values.
    Parameters:
        word_list: List of all the words in the world
    Returns:
        phenom_dict: A dictionary with the primary stresses as the keys
                    and the list of all the words containing the primary
                    stresses as their respective values.
    """
    phenom_dict = {}
    for lists in word_list:
        for i in range(len(lists)):
            if "1" in lists[i]:
                if lists[i] in phenom_dict:
                    phenom_dict[lists[i]].append(lists[0])
                else:
                    phenom_dict[lists[i]] = [lists[0]]
    return phenom_dict


def dict_build(filename):
    """
    This is a builder function which takes a file name and builds
    the spell_dict and phenom_dict.
    Parameters:
        filename: Name of the file to be read
    Returns:
        spell_dict: a dictionary with the words as the keys
                    and the list of their constituent phonemes
                    as their respective value.
        phenom_dict: A dictionary with the primary stresses as the keys
                    and the list of all the words containing the primary
                    stresses as their respective values.
    """
    word_list = file_read(filename)
    spell_dict = spell_to_pronunciation(word_list)
    phenom_dict = primary_phenom_dict(word_list)
    return spell_dict, phenom_dict


def word_extract(primary_stress, phenom_dict):
    """
    This function extracts words into list which contain primary stresses.
    Parameters:
        primary_stress: List of primary stresses of all pronunciations
                        of a given word.
        phenom_dict: A dictionary with the primary stresses as the keys
                    and the list of all the words containing the primary
                    stresses as their respective values.
    Returns:
        word_list: List of all the words in the world
    """
    word_list = []
    for i in range(len(primary_stress)):
        word_list.append(phenom_dict[primary_stress[i]])
    return word_list


def find_rhymes(primary_stress, matching_sequence, \
                non_matching_prev, word_list, spell_dict):
    """
    This function extracts words into list which contain primary stresses.
    Parameters:
        primary_stress: List of primary stresses of all pronunciations
                        of a given word.
        word_list: List of all the words in the world
        matching_sequence: The sequence after the matched primary in the
                        given word.
        non_matching_prev: The phoneme before the primary stress in the
                        given word.
        spell_dict: a dictionary with the words as the keys
                    and the list of their constituent phonemes
                    as their respective value.
    Returns:
        printed_words: The list of words that rhyme with given words.

    """
    printed_words = []
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            word_phenomes = spell_dict[word_list[i][j]]
            for k in range(len(word_phenomes)):
                if type(word_phenomes[0]) is list:
                    for l in range(len(word_phenomes[k])):
                        if word_phenomes[k][l] == primary_stress[i] and \
                                k != 0:
                            if word_phenomes[k][l - 1] != \
                                    non_matching_prev[i - 1] and \
                                    word_phenomes[k][l:] == \
                                    matching_sequence[i]:
                                if word_list[i][j] not in printed_words:
                                    printed_words.append(word_list[i][j])
                else:
                    if word_phenomes[k] == primary_stress[i] and k != 0:
                        if word_phenomes[k - 1] != non_matching_prev[i - 1] \
                                and word_phenomes[k:] == matching_sequence[i]:
                            if word_list[i][j] not in printed_words:
                                printed_words.append(word_list[i][j])
    return printed_words


def processing(primary_stress, word, phenom_dict, matching_sequence,\
               spell_dict, non_matching_prev):
    if len(primary_stress) == 0:
        print("Rhymes for: " + word)
        print(" -- none found -- ")
    else:
        word_list = word_extract(primary_stress, phenom_dict)
        print("Rhymes for: " + word)
        printed_words = \
            find_rhymes(primary_stress, matching_sequence, \
                        non_matching_prev, word_list, spell_dict)
        for i in range(len(printed_words)):
            print(printed_words[i])
        if len(printed_words) == 0:
            print(" -- none found -- ")


def main():
    """
    This is the function where all the programs run.
    """
    filename = input()
    spell_dict, phenom_dict = dict_build(filename)
    while 1:
        primary_stress, matching_sequence, non_matching_prev, phenom_list \
            = [], [], [], []
        try:
            word = input().strip().upper()
            if len(word.strip().split()) == 0:
                print("No word given")
            elif len(word.strip().split()) >= 2:
                print("Multiple words entered, please enter only" \
                      + "one word at a time.")
            elif word in spell_dict.keys():
                if type(spell_dict[word][0]) is list:
                    phenom_list = spell_dict[word]
                else:
                    phenom_list.append(spell_dict[word])
                for i in range(len(phenom_list)):
                    for j in range(len(phenom_list[i])):
                        if "1" in phenom_list[i][j] and j != 0:
                            primary_stress.append(phenom_list[i][j])
                            matching_sequence.append(phenom_list[i][j:])
                            non_matching_prev.append(phenom_list[i][j - 1])
                processing(primary_stress, word, phenom_dict, \
                           matching_sequence, spell_dict, non_matching_prev)
            else:
                print("Rhymes for: " + word)
                print(" -- none found -- ")
        except EOFError:
            break


if __name__ == '__main__':
    main()
