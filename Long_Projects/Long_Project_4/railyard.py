"""
Author: Nishant Athawale
Date: 26th April 2022
Class: CSC 120
Section Leader: Jason L'Italien 
Section : #5
Assignment: RE-Do Assignment Railyard
Description: This program animates one of the most common ways 
to win a tic tac toe game.
By default (unless you tell a function to return something else), 
all functions return None. None is actually a special type of object. 
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


def counter(yard):
    """
    This function calculates number of locomotives and unique destinations
    in a given railyard.
    Parameters:
        yard: The Railyard
    Returns:
         loco_counter   : Number of locomotives present in a given railyard.
         car_count      : Number of unique destinations in a given railyard.
    """
    loco_counter = 0
    car_count = 0
    destination_dict = {}
    for j in range(len(yard)):
        if len(yard[j]) != 0:
            if yard[j][0].lower() == "t":
                loco_counter += 1
            for i in range(len(yard[j])):
                if yard[j][i] not in destination_dict and yard[j][i] \
                        != "-" and yard[j][i].lower() != "t":
                    destination_dict[yard[j][i]] = 1
            car_count = len(destination_dict)
    return loco_counter, car_count


def print_output(yard, yard_len):
    """
    This function prints the output in a specified format.
    Parameters:
        yard:      The railyard in a 2-D list format
        yard_len:  A list containing lengths of different tracks in the
                    railyard (associated by Index).
    Returns:
        None
    """
    loco_count, car_count = counter(yard)
    for i in range(len(yard)):
        yard[i].reverse()
    for i in range(len(yard)):
        x = "".join(yard[i])
        print(f"{i + 1}: " + x.rjust(yard_len[i] - 1, "-") + "-")
    for i in range(len(yard)):
        yard[i].reverse()
    print(f"Locomotive count:  {loco_count}")
    print(f"Destination count: {car_count}\n")


def format_yard(filename):
    """
    This function reads a yard file converts a given yard into list of tracks,
     each of which contain each individual car as their elements.
    Parameters:
        filename: Name of the file to be read.
    Returns:
         yard:      The railyard in a 2-D list format
         tokenn:    A execution status variable
         yard_len:  A list containing lengths of different tracks in the
                    railyard (associated by Index).
    """
    yard_len = []
    yard = []
    try:
        tokenn = True
        text = open(filename, "r")
        for line in text:
            yard.append(list(reversed(line.strip())))
        for i in range(len(yard)):
            yard_len.append(len(yard[i]))
            yard[i] = list(filter("-".__ne__, yard[i]))
        print_output(yard, yard_len)
        return yard, tokenn, yard_len

    except FileNotFoundError or FileExistsError:
        print("ERROR: Could not open the yard file")
        tokenn = False
    return yard, tokenn, yard_len


def int_check(integer):
    """
    This function checks if the given argument is an integer or not.
    Parameters:
        integer:    A string which status is to be checked
    Return:
        True:       If the given string is an integer
        False:      Otherwise.
    """
    try:
        int(integer)
        return True
    except ValueError:
        return False


def split_cmd(cmd, yard, yard_len):
    """
    This splits the command string into its respective components
    and conducts the error checks.
    Parameters:
        cmd:        The command String
        yard:       The railyard
        yard_len:   A list containing lengths of different tracks in the
                    railyard (associated by Index).
    Returns:
        count:      Number of Cars to be moved
        to :        Destination of shifting
        fromm:      Origin of shifting
        True:       If any of the error conditions are true
        False:      If all the error conditions are False
        quit:       Status of the quit condition.
    """
    count, to, fromm, quit = 0, 0, 0, False
    cmd = cmd.strip().split()
    if cmd[0].lower() == "quit" and len(cmd) == 1:
        quit = True
    else:
        if ((cmd[0].lower() != "move") or (len(cmd) != 4)) or \
                (cmd[0].lower() == "quit" and len(cmd) > 1):
            print("ERROR: The only valid command formats are" \
                + "(where each X represents an integer):\nmove X X X\nquit\n")
        elif int_check(cmd[1]) is False:
            print(f"ERROR: Could not convert the 'count' value to an integer:\
            '{cmd[1]}'")
        elif int_check(cmd[2]) is False:
            print(f"ERROR: Could not convert the 'from-track' value to" \
                  + f" an integer:'{cmd[2]}'")
        elif int_check(cmd[3]) == False:
            print(f"ERROR: Could not convert the 'to-track' value to" \
                  + f" an integer:'{cmd[3]}'")
        elif cmd[3] == cmd[2]:
            print("ERROR: The 'to' track is the same as the 'from' track.")
        elif int(cmd[1]) < 0:
            print("ERROR: Cannot move a negative number of cars.")
        elif int(cmd[2]) <= 0 or int(cmd[3]) <= 0 or len(yard) < int(cmd[2]) \
                or len(yard) < int(cmd[3]):
            print("ERROR: The to-track or from-track number is invalid.")
        else:
            count, to, fromm = int(cmd[1]), int(cmd[3]), int(cmd[2])
            return count, to, fromm, True, quit
        print_output(yard, yard_len)
    return count, to, fromm, False, quit


def switch_check(yard, count, to, fromm, yard_len):
    """
    This function check for error conditions before switching cars
    Parameters:
    yard :  The railyard
    Count:  number of cars to be shifted
    to :    Destination of shifting
    fromm:  origin of shifting
    Returns:
    False:  If a error condition is observed
    True:   If no error Condition.
    """
    from_str = yard[fromm - 1][:]
    if yard[fromm - 1][0] == "T":
        from_str = from_str[1:]
    # if len(yard[fromm-1]) >= 0 and len(yard[to-1]) >= 0:
    if yard[fromm - 1][0] != "T" or len(yard[fromm - 1]) == 0:
        print(f"ERROR: Cannot move from track {fromm}" \
              + " because it doesn't have a locomotive.")
    elif len(yard[to - 1]) > 1 and yard[to - 1][0] == "T":
        print(f"ERROR: Cannot move to track {to} " \
              + "because it already has a locomotive.")
    elif len(from_str) < count:
        print(f"ERROR: Cannot move {count} cars from track {fromm}" \
              + " because it doesn't have that many cars.")
    elif (len(yard[to - 1]) + count) + 1 > yard_len[to - 1] - 2:
        print(f"ERROR: Cannot move {count} cars to track {to} " \
              + "because it doesn't have enough space.")
    else:
        return True
    return False


def switch_tracks(yard, count, to, fromm, yard_len):
    """
    This function switches tracks of desired number
    of cars and locomotive
    Parameters:
    yard :  The railyard
    Count:  number of cars to be shifted
    to :    Destination of shifting
    fromm:  origin of shifting
    Returns:
    yard:   The updated yard after train switch.
    """
    status = switch_check(yard, count, to, fromm, yard_len)
    if status is True:
        temp = []
        temp = yard[fromm - 1][:count + 1]
        yard[fromm - 1] = yard[fromm - 1][count + 1:]
        temp += yard[to - 1]
        yard[to - 1] = temp
        print(f"The locomotive on track {fromm} moved " \
              + f"{count} cars to track {to}.\n")

    return yard


def yeet_check(yard, yard_len):
    """
    This function Checks if Train is ready to depart
    Parameters:
    yard :  The railyard

    Returns:
    None:   If at least one locomotive in yard
    True:   If All locomotives departed.
    """
    loco_count, dest_count = counter(yard)
    yeet, donee = 0, False
    for i in range(len(yard)):
        if len(yard[i]) != 0 and yard[i][0] == "T":
            init, check, car_count = None, True, 0
            for j in range(len(yard[i])):
                if yard[i][j].lower() != "t":
                    car_count += 1
                    if init is None:
                        init = yard[i][j]
                    elif yard[i][j] != init:
                        check = False
                        break
            if check == True and len(yard[i]) > 1:
                yeet = 1
                for k in range(len(yard)):
                    yard[k].reverse()
                for k in range(len(yard)):
                    x = "".join(yard[k])
                    print(f"{k + 1}: " + x.rjust(yard_len[k] - 1, "-") + "-")
                yard[i] = []
                for k in range(len(yard)):
                    yard[k].reverse()
                print(f"*** ALERT***  The train on track {i + 1}, which had " \
                      + f"{car_count} cars, departs for destination {init}.\n")
                loco_count, dest_count = counter(yard)
                if loco_count == 0:
                    print("The last locomotive has departed!")
                    print_output(yard, yard_len)
                    return True
                print_output(yard, yard_len)
    if yeet == 0:
        print_output(yard, yard_len)


def play_game(yard, yard_len):
    """
    This function runs the game
    Parameters:
    yard :      The Grid of the Rail yard
    Returns:    None
    """
    cmd = input("What is your next command?\n")
    while 1:
        token = True
        count, to, fromm, tokenn, quit = split_cmd(cmd, yard, yard_len)
        if tokenn is True:
            yard = switch_tracks(yard, count, to, fromm, yard_len)
            donee = yeet_check(yard, yard_len)
            if donee is True:
                break
            cmd = input("What is your next command?\n")
        elif quit is True and tokenn is False:
            print("Quitting!")
            break
        else:
            cmd = input("What is your next command?\n")


def main():
    filename = input("Please give the yard file:\n")
    yard, tokenn, yard_len = format_yard(filename)
    if tokenn is True:
        play_game(yard, yard_len)


if __name__ == "__main__":
    main()
