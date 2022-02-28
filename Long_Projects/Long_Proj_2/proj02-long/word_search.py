"""
Author: Nishant Athawale
Date: 1st February 2022
Class: CSC 120
Section Leader: Jason L'Italien 
Section : #5
Description: This program finds words given in a list and highlights 
them on console by replacing all other letters with period.
By default (unless you tell a function to return something else), 
all functions return None. None is actually a special type of object. 
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""

def read_file(text):
    '''
    This function reads the text file and does two things:
    1. Create a grid for the word search
    2. Creates a list of words to be searched.
    Parameters:
    text :  The file which is to be processed
        
    Returns:
    grid: The grid on which the words are to be searched
    word: List of words to be searched on the grid 
    '''
    grid = []
    row = []
    word = []
    grid_read = True
    for lines in text:
        if len(lines.strip()) == 0: 
            grid_read = False

        else:
            if grid_read == True:
                line = lines.strip()
                for char in line:
                    row.append(char)
                grid.append(row)
                row = []
            else:
                word.append(lines.strip())
    return grid ,word

def grid_format(grid):
    '''
    It transforms the grid to resemble a cartesian system
    ^
    |
    |
    | 
    |_________>
  (0,0)
    Parameters:
    grid : The grid to be transformed
    Returns: 
    grid : Returns the transformed grid.
    '''
    formatted_grid = []
    for i in range(len(grid),0,-1):
        formatted_grid.append(grid[i-1])
    return(formatted_grid)

def linear_check(grid,x_index,y_index,word_len):
    '''
    This function checks whether if the string of given word is possible
    in horizonatal and vertical directions.
    Parameters:
    grid : The grid which is to be searched
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word_len : Length of the word to be search
     
    Returns: 
    n: A boolean confirming whether the desired string is possible 
    in north direction
    s: A boolean confirming whether the desired string is possible 
    in south direction
    e: A boolean confirming whether the desired string is possible 
    in east direction
    w: A boolean confirming whether the desired string is possible 
    in north direction
    '''
    n,s,e,w = True,True,True,True
    grid_height = len(grid)
    grid_width = len(grid[0])
    if x_index - word_len < 0:
        w = False
    if x_index + word_len > grid_width:
        e = False
    if y_index - word_len < 0:
        s = False
    if y_index + word_len > grid_height:
        n = False
    return n,s,e,w


def vertical_words(grid,y_index,x_index,word_len):
    '''
    This function extracts strings from the grid in 
    north, south ,east and west direction
    Parameters:
    grid: Grid from which strings are to be extracted
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word_len : Length of the word to be search
    
    Returns: 
    north: string extracted in north direction
    south: string extracted in south direction
    east: string extracted in east direction
    west: string extracted in west direction
    '''
    north_counter,south_counter,east_counter,west_counter = \
        y_index,y_index,x_index,x_index
    north,south,east,west = "","","",""
    n,s,e,w = linear_check(grid,x_index,y_index,word_len)
    for i in range(word_len):
        if n == True:
            north += grid[north_counter][x_index]
        if s == True:    
            south += grid[south_counter][x_index]  
        
        north_counter += 1
        south_counter -= 1  
        
        if e ==True:    
            east += grid[y_index][east_counter]
        if w == True:    
            west += grid[y_index][west_counter]
        
        east_counter += 1
        west_counter -= 1
    return north,south,east,west
    

def linear_direction(grid,y_index,x_index,word,word_len):
    '''
    This function finds whether the desired word is in 
    north, south, east or west direction.
    Parameters:
    grid: Grid from which strings are to be extracted
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word: The word to be searched
    word_len : Length of the word to be search
    Returns: 
    If the word is in the grid : north/south/east/west
    If the word is not on the grid : None
    '''
    north,south,east,west = vertical_words(grid,y_index,x_index,word_len)
    status = False
    if east == word:
        return "east"
    elif west == word:
        return "west" 
    elif north == word:
        return "north"
    elif south == word:
        return "south"
    return None

def diagonal_check(grid,x_index,y_index,word_len):
    '''
    This function checks whether if the string of given word is possible
    in horizonatal and diagonal directions.
    Parameters:
    grid : The grid which is to be searched
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word_len : Length of the word to be search
     
    Returns: 
    nw: A boolean confirming whether the desired string is possible 
    in northwest direction
    ne: A boolean confirming whether the desired string is possible 
    in northeast direction
    sw: A boolean confirming whether the desired string is possible 
    in southwest direction
    se: A boolean confirming whether the desired string is possible 
    in southeast direction
    '''
    nw,ne,sw,se = True,True,True,True
    grid_height = len(grid)
    grid_width = len(grid[0])
    if (x_index+word_len > grid_width) or (y_index +word_len > grid_height):
        ne = False
    if (x_index-word_len) < 0 or (y_index +word_len > grid_height):
        nw = False
    if (x_index-word_len < 0) or (y_index -word_len < 0):
        sw = False
    if (x_index+word_len > grid_width) or (y_index -word_len < 0):
        se = False
    return(nw,ne,sw,se)
    
def diagonal_words(grid,y_index,x_index,word_len):
    '''
    This function extracts strings from the grid in 
    northwest, southeast ,northeast and southwest direction
    Parameters:
    grid: Grid from which strings are to be extracted
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word_len : Length of the word to be search
    
    Returns: 
    northwest: string extracted in northwest direction
    southeast: string extracted in southeast direction
    northeast: string extracted in northeast direction
    southwest: string extracted in southwest direction
    '''
    north_counter,south_counter,east_counter,west_counter = \
        y_index,y_index,x_index,x_index
    nw,ne,sw,se = diagonal_check(grid,x_index,y_index,word_len)
    south_w,south_e,north_w,north_e = "","","",""
    for i in range(word_len):
        if ne == True:
            north_e += grid[north_counter][east_counter]
        if se == True:    
            south_e += grid[south_counter][east_counter]  
        if sw ==True:    
            south_w += grid[south_counter][west_counter]
        if nw == True:    
            north_w += grid[north_counter][west_counter]
        
        east_counter += 1
        west_counter -= 1
        north_counter += 1
        south_counter -= 1
    return south_w,south_e,north_w,north_e  


def diagonal_direction(grid,y_index,x_index,word,word_len):

    '''
    This function finds whether the desired word is in 
    northeast, southwest, southeast or northwest direction.
    Parameters:
    grid: Grid from which strings are to be extracted
    x_index: x co-oridnate of the instance of the first letter of the 
    given word.
    y_index: y co-ordinate of the instance of the first letter of the 
    given word.
    word: The word to be searched
    word_len : Length of the word to be search
    Returns: 
    If the word is in the grid : northeast/southwest/southeast/northwest
    If the word is not on the grid : None
    '''
    south_w,south_e,north_w,north_e = \
        diagonal_words(grid,y_index,x_index,word_len)
    if south_e == word:
        return("southeast")
    if south_w == word:
        return("southwest")
    if north_e == word:
        return("northeast")
    if north_w == word:
        return("northwest")
    return None

def print_grid(y_index,x_index,direction,grid,word):
    '''
    This function inserts the word in its location 
    in a grid of periods (".") and then prints this final grid.
    Parameters:
    y_index: y co-oridnate of the instance of the first letter of the 
    given word.
    x_index: x co-ordinate of the instance of the first letter of the 
    given word.
    direction: The direction in which the word is found on the grid.
    grid: Grid in which word is to be searched.
    word: The word to be printed on the grid
    
    Returns: None
    '''
    final_grid = []
    row = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            row.append(".")
        final_grid.append(row)
        row = []
    word = list(word)
    for i in range(len(word)):
        if direction == "east":    
            final_grid[y_index][x_index+i] = word[i]
        elif direction == "west":
            final_grid[y_index][x_index-i]= word[i]
        elif direction == "south":
            final_grid[y_index-i][x_index]= word[i]
        elif direction == "north":
            final_grid[y_index+i][x_index]= word[i]
        elif direction == "southeast":
            final_grid[y_index-i][x_index+i] = word[i]
        elif direction == "southwest":
            final_grid[y_index-i][x_index-i] = word[i]
        elif direction == "northeast":
            final_grid[y_index+i][x_index+i] = word[i]
        elif direction == "northwest":
            final_grid[y_index+i][x_index-i] = word[i]
    final_grid = grid_format(final_grid)
    for i in range(len(final_grid)):
        print("".join(final_grid[i]))


def word_search(grid,word_set):
    '''
    This function finds the words in a given list in the 
    given grid.
    Parameters:
    grid : Grid in which words are to be searched.
    word_set: list of words that are to be searched.
    
    Returns: 
    None
    '''
    for word in word_set:
        status = False
        initial_char = word[0]
        word_len = len(word)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == initial_char:
                    linear_status = linear_direction(grid,i,j,word,word_len)
                    diagonal_status = \
                        diagonal_direction(grid,i,j,word,word_len)
                    if linear_status != None:
                        print_grid(i,j,linear_status,grid,word)
                        status = True
                    elif diagonal_status != None:
                        print_grid(i,j,diagonal_status,grid,word)
                        status = True

        if status == False:
            print(f"Word '{word}' not found")


def main():
    print("Please give the puzzle filename:")
    filename = input()
    try:
        text = open(filename,'r')
        grid , words = read_file(text)  
        updated_grid = grid_format(grid)
        status = word_search(updated_grid,words)

    except FileNotFoundError or FileExistsError:
        print("Sorry, the file doesn't exist or cannot be opened.")
if __name__ == '__main__':
    main()