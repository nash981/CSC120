
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


import os

def main():
    # chdir to the same directory as where this script is ... so
    # that open() will open the file we expect.
    this_script = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)
    states = []
    state_count = 0
    total_population = 0
    filename = input("file: ")
    text = open(filename,'r')
    for lines in text:
        if lines[0] =="#" or len(lines.strip()) == 0:
            continue
        else:
            elements = lines.strip().split()
            population = elements[-1]
            state = " ".join(elements[:-1])
            if state not in states :
                states += state
                state_count +=1
            print("State/Territory:".ljust(17," ")+f"{state}")
            print("Population:".ljust(17," ")+ f"{population}")
            print("")
            total_population += int(population)
    print("")
    print("# of States/Territories: ".ljust(25," ")+f"{state_count}")
    print("Total Population:".ljust(25," ")+ f"{total_population}")

            


if __name__ == '__main__':
    main()