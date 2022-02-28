"""
Author: Nishant Athawale
Date: 8th February 2022
Class: CSC 120
Section Leader: Jason L'Italien 
Section : #5
Description: This program animates one of the most common ways 
to win a tic tac toe game.
By default (unless you tell a function to return something else), 
all functions return None. None is actually a special type of object. 
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""

def counter(yard):
    '''
    This function creates the grid.
    Parameters:
            
    Returns: 
    '''
    loco_counter = 0
    car_count = 0
    destination_dict={}
    for j in range(len(yard)):
        if len(yard[j]) != 0:    
            if yard[j][0].lower() == "t":
                loco_counter+=1
            for i in range(len(yard[j])):
                if yard[j][i] not in destination_dict and yard[j][i] \
                    != "-" and yard[j][i].lower() != "t" :
                    destination_dict[yard[j][i]] = 1
            car_count = len(destination_dict)
    return(loco_counter,car_count)


def print_output(yard):
    '''
    This function creates the grid.
    Parameters:
            
    Returns: 
    '''
    loco_count,car_count = counter(yard)
    for i in range(len(yard)):
        yard[i].reverse()
    for i in range(len(yard)):
        x = "".join(yard[i])
        print(f"{i+1}: "+x.rjust(21,"-")+"-")
    for i in range(len(yard)):
        yard[i].reverse()
    print(f"Locomotive count:  {loco_count}")
    print(f"Destination count: {car_count}\n")
    

        
def format_yard(filename):
    '''
    This function creates the grid.
    Parameters:
            
    Returns: 
    '''
    yard = []
    try:
        tokenn = True
        text  = open(filename,"r")
        for line in text:
            yard.append(list(reversed(line.strip())))    
        for i in range(len(yard)):
            yard[i] = list(filter(("-").__ne__, yard[i]))    
        print_output(yard)
        return yard,tokenn
        
    except FileNotFoundError or FileExistsError:
        print("ERROR: Could not open the yard file") 
        tokenn = False
    return yard,tokenn   
    
def split_cmd(cmd,yard):
    '''
    This function creates the grid.
    Parameters:
            
    Returns: 
    '''
    count,to,fromm,quit = 0,0,0,False
    cmd = cmd.strip().split(" ")
    if cmd[0].lower() == "quit":
        quit = True        
    else:
        if (cmd[0].lower() != "move") or (len(cmd)!= 5):
            print("ERROR: The only valid command formats are" \
            +"(where each X represents an integer):\nmove X X X\nquit\n")
        elif (cmd[2].isdigit() == False):
            print(f"ERROR: Could not convert the 'count' value to an integer:\
            '{cmd[2]}'")
        elif (cmd[3].isdigit() == False):
            print(f"ERROR: Could not convert the 'from-track' value to" \
            +f" an integer:'{cmd[3]}'")
        elif (cmd[4].isdigit() == False):
            print(f"ERROR: Could not convert the 'to-track' value to"\
            +f" an integer:'{cmd[4]}'")
        elif cmd[4] == cmd[3]:
            print("ERROR: The 'to' track is the same as the 'from' track.")
        elif int(cmd[2])<0:
            print("ERROR: Cannot move a negative number of cars.")
        elif int(cmd[3])<0 or int(cmd[4])<0 or len(yard)<int(cmd[3])\
            or len(yard)<int(cmd[4]):
            print("ERROR: The to-track or from-track number is invalid.")
        else:
            count,to,fromm = int(cmd[2]),int(cmd[4]),int(cmd[3])
            return count,to,fromm,True,quit
        print_output(yard)
    return count,to,fromm,False,quit

def switch_check(yard,count,to,fromm):
    '''
    This function check for error conditions 
    before switching cars
    Parameters:
    yard : The railyard
    Count: number of cars to be shifted
    to : Destination of shifting
    fromm: origin of shifting   
            
    Returns: 
    False: If a error condition is observed
    True: If no error Condition.
    '''
    tokenn = False
    if(len(yard[fromm-1])>=0 and len(yard[to-1])>=0):
        if yard[fromm-1][0] != "T" or len(yard[fromm-1]) == 0:
            print(f"ERROR: Cannot move from track {fromm}"\
            +" because it doesn't have a locomotive.")
        elif  len(yard[to-1])>0 and yard[to-1][0] == "T":
            print(f"ERROR: Cannot move to track {to} "\
            +"because it already has a locomotive.")
        elif len(yard[fromm-1])<count:
            print(f"ERROR: Cannot move {count} cars from track {fromm}"\
            +" because it doesn't have that many cars.")
        elif (len(yard[to-1])+count) > 20:
            print(f"ERROR: Cannot move {count} cars to track {to} "\
            +"because it doesn't have enough space.")
        else:
            return (True)
    return(False)

def switch_tracks(yard,count,to,fromm):
    '''
    This function switches tracks of desired number 
    of cars and locomotive
    Parameters:
    yard : The railyard
    Count: number of cars to be shifted
    to : Destination of shifting
    fromm: origin of shifting   
    Returns: 
    yard: The updated yard after train switch. 
    '''
    status = switch_check(yard,count,to,fromm)
    if status == True :
        temp = []
        temp = yard[fromm-1][:count+1]
        yard[fromm-1]= yard[fromm-1][count+1:]
        temp += yard[to-1]
        yard[to-1] = temp 
        print(f"The locomotive on track {fromm} moved " \
        + f"{count} cars to track {to}.\n")
        
    return yard

def yeet_check(yard):
    '''
    This function Checks if Train is ready to depart
    Parameters:
    yard : The railyard
            
    Returns: None If atleast one locomotive in yard
    True if All locomotives departed.
    '''
    loco_count,dest_count = counter(yard) 
    yeet,donee = 0,False
    for i in range (len(yard)):
        if len(yard[i]) != 0 and yard[i][0] == "T":
            init,check,car_count = None,True,0
            for j in range(len(yard[i])):
                if yard[i][j].lower() != "t":
                    car_count += 1
                    if init == None:
                        init = yard[i][j]
                    elif yard[i][j] != init:
                        check = False
                        break
            if check == True and len(yard[i])>1:
                yeet = 1
                yard[i] = []
                loco_count,dest_count = counter(yard)
                for i in range(len(yard)):
                    yard[i].reverse()
                for i in range(len(yard)):
                    x = "".join(yard[i])
                    print(f"{i+1}: "+x.rjust(21,"-")+"-")
                for i in range(len(yard)):
                    yard[i].reverse()
                print(f"*** ALERT***  The train on track {i+1}, which had "\
                +f"{car_count} cars, departs for destination {init}.\n")
                if loco_count == 0:
                    print("The last locomotive has departed!")
                    print_output(yard)
                    return True
                print_output(yard)
    if yeet == 0:    
        print_output(yard)

def play_game(yard):
    '''
    This function runs the game
    Parameters:
    yard : The Grid of the Rail yard 
    Returns:  None
    '''
    cmd = input("What is your next command ?")
    print("\n")
    while(1):
        token = True
        count,to,fromm,tokenn,quit = split_cmd(cmd,yard)
        if tokenn == True:
            yard = switch_tracks(yard,count,to,fromm)
            donee = yeet_check(yard)
            if donee == True:
                break
            cmd = input("What is your next command ?\n")
        elif quit == True and tokenn == False:
            print("Quitting!")
            break
        else:
            cmd = input("What is your next command ?")


def main():
    filename = input("Please give the yard file:\n")
    yard,tokenn = format_yard(filename)
    if tokenn == True:    
        play_game(yard)

    


if __name__ == "__main__":
    main()