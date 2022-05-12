
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
  
    status = True
    running_total = 0
    total_lines = 0
    number_total = 0
    blank_line = 0

    while(status):
        line = input().strip()
        numbers = line.split()
        total_lines+=1
        for numb in numbers:
            if int(numb) == -1:
                status == False
                return None
            
            else:
                running_total += int(numb)
                number_total+=1
                print(f"Total:{running_total} - \
                    numbers:{number_total} total_lines:\
                        {total_lines} blank_lines:{blank_line}")

        if numbers == []:
            blank_line += 1

        
    
    


if __name__ == '__main__':
    main()