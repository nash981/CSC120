
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

def main():
    
    input_string = input("input string: ")
    print(len(input_string))
    print(input_string[1])
    print(input_string[:10])
    print(input_string[-5:])
    print(input_string.upper())
    if input_string[0].lower() in "qwerty":
        print("QWERTY")
    elif input_string[0] in "uiop":
        print("UIOP")
    elif input_string[0].lower() in \
         "alskdjfhgzmxncbv" or input_string[0] in "UIOP":
        print("LETTER")
    elif input_string[0].isdigit():
        print("DIGIT")
    else:
        print("OTHERS")
    num1 = input()
    num2 = input()
    product = int(num1)*int(num2)
    print(product)



if __name__ == '__main__':
    main()