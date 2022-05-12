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

import graphics

def create_grid(inst):
    '''
    This function creates the grid.
    Parameters:
    inst: The graphics object        
    Returns: None
    '''
    inst.line(0,300,900,300,width=7)
    inst.line(0,600,900,600,width=7)
    inst.line(300,0,300,900,width=7)
    inst.line(600,0,600,900,width=7)

def draw_x(x_a_1,y_a_1,x_a_2,y_a_2,x_b_1,y_b_1,x_b_2,y_b_2,inst):
    '''
    This function draws x in a given position of grid
    Parameters:
    x_a_1 : x co-ordinate of the starting point of line with decreasing slope.
    y_a_1 : y co-ordinate of the starting point of line with decreasing slope.
    x_a_2 : x co-ordinate of the ending point of line with decreasing slope.
    y_a_2 : y co-ordinate of the ending point of line with decreasing slope.
    x_b_1 : x co-ordinate of the starting point of line with increasing slope.
    y_b_1 : y co-ordinate of the starting point of line with increasing slope.
    x_b_2 : x co-ordinate of the ending point of line with increasing slope.
    y_b_2 : y co-ordinate of the ending point of line with increasing slope.
    inst: The graphics object.        
    Returns: None
    '''
    inst.update_frame(1)
    inst.line(x_a_1,y_a_1,x_a_2,y_a_2,width=7,fill="orange")
    inst.line(x_b_1,y_b_1,x_b_2,y_b_2,width=7,fill="orange")

def draw_o(x,y,d,inst):
    '''
    This function draws O in a given position of grid
    x : x co-ordinate of the centre of the ellipse
    y : y co-ordinate of the centre of the ellipse
    d : diameter of the circle
    inst : The graphics object
    Returns : None
    '''
    inst.update_frame(1)
    inst.ellipse(x,y,d,d,fill="red")





def main ():
    inst = graphics.graphics(900,900,"ti_ta_to")
    inst.rectangle(0,0,900,900,fill = "skyblue")
    create_grid(inst)
    while (inst.is_destroyed() != True):
        draw_x(650,50,850,250,650,250,850,50,inst)
        draw_o(150,750,200,inst)
        draw_x(650,650,850,850,650,850,850,650,inst)
        draw_o(750,450,200,inst)
        draw_x(50,50,250,250,50,250,250,50,inst)
        draw_o(450,450,200,inst)
        draw_x(350,50,550,250,350,250,550,50,inst)
        inst.line(0,150,900,150,width = 9,fill = "black")


if __name__ == "__main__":
    main()