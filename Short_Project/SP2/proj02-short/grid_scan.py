# Author: Nishant Athawale
# Date: 27th January 2022
# Class: CSC 120
# Section Leader: Jason L'Italien 
# Section : #5
# By default (unless you tell a function to return something else), 
# all functions return None. None is actually a special type of object. 
# This is important because if None is a value, "returns nothing,"
# "doesn't return anything," and "no returns" are incorrect.

def final_out(grid,grid_length,grid_height):
    # This function prints the final grid after  
    # formatting.

    # Parameters:
    # grid -> Grid to be printed
    # grid_length -> Length of the grid
    # grid_height -> Height of the grid
    # Returns: None
    for i in range(int(grid_height)-1,-1,-1):
        grid[i] = "".join(grid[i])
        print(grid[i])

def char_search(direction,x,y,steps,grid):
    # This function traverses the grid from   
    # a specified position for given number of steps. 
    # The character in each space is recorded and then
    # replaced by the period "." character.

    # Parameters:
    # direction -> Direction in which grid is to be traversed.
    # x -> x - co-ordinate of the starting point.
    # y -> y - co-ordinate of the starting point.
    # steps -> number of steps to be traversed on the grid.y_index.
    # grid -> grid which is to be traversed.
    # Returns: None
    try:    
        grid_length=(len(grid[0]))
        grid_height = len(grid)
        return_str = ""
        x_index = int(x)
        y_index = int(y)
        if direction.upper() == "N":
            for i in range(int(steps)):
                return_str+=grid[y_index][x_index]
                grid[y_index][x_index] = "."
                y_index+=1       
            print(return_str) 
        elif direction.upper() == "E": 
            for i in range(int(steps)):
                return_str+=grid[y_index][x_index]
                grid[y_index][x_index] = "."
                x_index+=1   
            print(return_str)     
        elif direction.upper() == "SW":
            for i in range(int(steps)):
                return_str+=grid[y_index][x_index]
                grid[y_index][x_index] = "."
                x_index-=1
                y_index -=1   
            print(return_str)   
        else:
            print("INVALID DIRECTION")
        print("")
        final_out(grid,grid_length,grid_height)
    except IndexError:
        print(f"ERROR: Could not collect {steps} letters,\
 starting at ({x},{y}),because it fell off of the grid.")


def main():
    filename = input()
    command = input()
    grid = open(filename,'r')
    formatted_grid = []
    inner_grid = []
    outer_grid =[]
    for line in grid: 
        if len(line.strip()) != 0:
            for char in line.strip():   
                inner_grid.append(char)
            outer_grid.append(inner_grid)
        inner_grid =[]

    for i in range(len(outer_grid),0,-1):
        formatted_grid.append(outer_grid[i-1])
    command = command.strip().split()
    char_search(command[0],command[1],command[2],command[3],formatted_grid)
    





if __name__ == '__main__':
    main()