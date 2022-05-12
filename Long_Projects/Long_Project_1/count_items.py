
# Author: Nishant Athawale
# Date: 25th January 2022
# Class: CSC 120
# Section Leader: Jason L'Italien 
# Section : #5

# Description:
# This is aimed to test the python basics.

# By default (unless you tell a function to return something else), 
# all functions return None. None is actually a special type of object. 
# This is important because if None is a value, "returns nothing,"
# "doesn't return anything," and "no returns" are incorrect.


def print_step1(keylist,dict):
    
    # This function prints the original dictionary 
    # present in the file, in a specified format.

    # Parameters:
    # keylist -> List of keys that are present in the dictionary.
    # dict -> The dictionary which is to be printed.
    # Returns: None
    
    print("STEP 1: THE ORIGINAL DICTIONARY")
    for keys in keylist:
        print(f"  Key: {keys} Value: {dict[keys]}")

def step_2_step_3(dict,keylist):
    # This function creates a list of tuples consisting
    # value-key pairs before sorting.
    # Then it sorts the list lexically, prints it and 
    # returns the tuple list.

    # Parameters:
    # keylist -> List of keys that are present in the dictionary.
    # dict -> The dictionary which is to be printed.
    # Returns: 
    # tuple_list -> A list of sorted tuples. 

    tuple_list=[]
    for keys in keylist:
        tuple_list.append((int(dict[keys]),keys))
    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    print(tuple_list)
    print("STEP 3: AFTER SORTING")
    tuple_list.sort()
    print(tuple_list)
    return(tuple_list)
        
def step_4(tuple_list):
    # This function prints the expected out put in a 
    # specified formats.
    # Parameters:
    # tuple_list -> A list of sorted tuples. 
    # Returns: None 
    print("STEP 4: THE ACTUAL OUTPUT")
    for tuples in tuple_list:
        print(f"{tuples[1]} {tuples[0]}" )

def main ():
    filename = input("File to scan: ")
    dict_1 = {}
    keylist = []
    text = open(filename, "r")
    for lines in text:
        if len(lines.strip()) != 0:
            data_list = lines.strip().split()
            if data_list[0] in keylist:
                dict_1[data_list[0]] += int(data_list[1])
            else:
                dict_1[data_list[0]] = int(data_list[1])
                keylist.append(data_list[0])
    keylist.sort()
    print_step1(keylist,dict_1)
    tuple_list = step_2_step_3(dict_1,keylist)
    step_4(tuple_list)
    
    



if __name__ == '__main__':
    main()