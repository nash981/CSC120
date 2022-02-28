

def match_check(guess,correct,match_list):
    for i in range(len(guess)):
        if guess[i] == correct[i]:
            match_list[i]=1
            guess[i] = "."
            correct[i] = "." 
    return guess , correct , match_list
    
def missed_check(guess_residue,correct_residue,miss_list):
    letter_dict = {}
    for i in range(len(guess_residue)):
        if guess_residue[i] in correct_residue and guess_residue[i] != ".":
            if guess_residue[i] in letter_dict.keys():
                letter_dict[guess_residue[i]] +=1
            else:
                letter_dict[guess_residue[i]]=1   
    for i in range(len(guess_residue)):
        if guess_residue[i] in correct_residue and guess_residue[i] != ".":
            if guess_residue[i] in letter_dict.keys() and \
                letter_dict[guess_residue[i]] != 0:
                miss_list[i] = 1
                letter_dict[guess_residue[i]] -= 1
                

    return miss_list

def output(guess,correct,match_list,miss_list):
    miss_string = ""
    match_string = ""
    for i in range(len(guess)):
        if match_list[i] == 1:
            match_string += guess[i]
            miss_string += "."
        elif miss_list[i] == 1:
            miss_string += guess[i]
            match_string += "."
        else: 
            miss_string+="."
            match_string+="."
    correct = "".join(correct)
    guess ="".join(guess)
    return match_string,miss_string

def print_output(match_string,miss_string,guess,correct):
    print("Correct:".ljust(9," ")+f"{correct}")
    print("Guess".ljust(9," ")+f"{guess}")
    print("----")
    print("Match:".ljust(9," ")+f"{match_string}")
    print("Miss:".ljust(9," ")+f"{miss_string}")



def check(guess,correct):
    guess_list = list(guess.upper().strip())
    correct_list = list(correct.upper().strip())
    word_len = len(correct)
    match_list , miss_list = [] , []
    for i in range(word_len):
        match_list.append(0)
        miss_list.append(0)
    guess_residue, correct_residue,match_list = \
        match_check(guess_list,correct_list,match_list)
    miss_list = missed_check(guess_residue,correct_residue,miss_list)
    match_string, miss_string = output(list(guess.upper().strip()),\
        list(correct.upper().strip()),match_list,miss_list)
    return("".join(match_string),"".join(miss_string))

def missmatch(match,miss,filtered_set,keys,miss_charset):
    temp_set = set()
    for i in range(len(keys)):
            for word in filtered_set:
                if (word[keys[i]] == match[keys[i]]):
                    temp_set.add(word)
            filtered_set = set()
            filtered_set=temp_set
            temp_set = set()
    return filtered_set
    


def miss_match(match,miss,filtered_set,keys,miss_charset):
    temp_set = set()
    if len(miss_charset) == 0:
        for i in range(len(keys)):
            for word in filtered_set:
                if (word[keys[i]] == match[keys[i]]):
                    temp_set.add(word)
            filtered_set = set()
            filtered_set=temp_set
            temp_set = set()
    elif len(keys) == 0:
        for i in range(len(miss_charset)):
            for word in filtered_set:
                if miss_charset[i] in word:
                    temp_set.add(word)
            filtered_set = set()
            filtered_set=temp_set
            temp_set = set()
    else: 
        final_set = set()
        final_set  = missmatch(match,miss,filtered_set,keys,miss_charset)
        filtered_set = set()
        filtered_set = final_set
    return filtered_set
    

def word_filter(match,miss,words):
    keys ,miss_charset = [],[] 
    length = len(match)
    temp_set,filtered_set = set(),set()
    for i in range(len(miss)):
        if match[i] != ".":
                keys.append(i)
        if miss[i] != ".":
            miss_charset.append(miss[i])
    for items in words: 
        for i in range(length):
            if match[i] == items[i]:
                filtered_set.add(items)
            elif miss[i] in items:      
                filtered_set.add(items) 
    final_set = miss_match(match,miss,filtered_set,keys,miss_charset)
    return(final_set)

    

def main():
    x =0

if __name__ == "__main__":
    main()