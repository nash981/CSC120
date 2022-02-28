"""
    Author: Nishant Athawale
    Date: 22nd February 2022
    Class: CSC 120
    Section Leader: Jason L'Italien
    Section : #5
    Description:
    This is aimed to practice linked lists and classes.

    By default (unless you tell a function to return something else),
    all functions return None. None is actually a special type of object.
    This is important because if None is a value, "returns nothing,"
    "doesn't return anything," and "no returns" are incorrect.
"""


class Grid:
    """
        This class represents one room in a grid.  It can contain any number
        of rooms in north, south, east and west direction .

        The constructor builds an empty room; you must pass it
        references to the four adjacent rooms (each might be None) - ≈
        references to the reconfigured later.

        The class defines several helpful methods and fields:
            setter():     - setter function for the 4 different
            directions.
            set_name():   - setter function for name field
            get_name():   - getter function for name field
            collapse_room() - This function sets all the links of a
            particular room to None. It also sets the links of the
            adjacent rooms point towards itself to None

       """
    def __init__(self):
        self._name = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None
        self.val = None

    def setter(self, north, south, east, west):
        """
            This function links the adjacent rooms to the current room
            object by populating the north, south, east and west fields
            with the room objects in the respective directions.

            Parameters:
                self:   This refers to the object itself
                north:  This refers to the object to the north of
                correct object
                south:  This refers to the object to the south of
                correct object
                east:   This refers to the object to the east of
                correct object
                west:   This refers to the object to the west of
                correct object

            Returns: None
        """
        self.n = north
        self.s = south
        self.e = east
        self.w = west
        self.val = "."

    def set_name(self, name):
        """
            This function sets the name of the object
            Parameters:
                self:   This refers to the object itself
                name:   This is the name of the object
            Returns: None
        """
        self._name = name

    def get_name(self):
        """
            This function returns the name of the object
            Parameters:
                self:   This refers to the object itself
            Returns:
                The name of the object
        """
        return str(self._name)

    def collapse_room(self):
        if self.n is not None:
            self.n.s = None
            self.n = None
        if self.s is not None:
            self.s.n = None
            self.s = None
        if self.e is not None:
            self.e.w = None
            self.e = None
        if self.w is not None:
            self.w.e = None
            self.w = None


def populate_grid(wid, hei, obj_grid):
    """
    This function links the adjacent rooms by populating the
    north, south, east and west fields with the room objects
    in the respective directions

    Parameters:
        wid: Width of the grid
        hei: Height of the grid
        obj_grid: A grid of objects that are to be linked.

    Returns:
        This function returns the south-west corner of the grid.
    """
    north, south, east, west = None, None, None, None
    for i in range(hei):
        for j in range(wid):
            if i is 0:
                if j is 0:
                    north, south, east, west = None, obj_grid[i+1][j], \
                                               obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = None, obj_grid[i+1][j], \
                        obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = None, obj_grid[i+1][j], \
                                               None, obj_grid[i][j-1]
            elif 0 < i < hei-1:
                if j is 0:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], None, obj_grid[i][j-1]
            elif i is hei-1:
                if j is 0:
                    north, south, east, west = obj_grid[i-1][j], None, \
                                               obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = obj_grid[i-1][j], None, \
                        obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = obj_grid[i-1][j], None, \
                                               None, obj_grid[i][j-1]
            obj_grid[i][j].set_name(str(f"{i}{i}{j}"))
            obj_grid[i][j].setter(north, south, east, west)
    return obj_grid[hei-1][0]


def build_grid(wid, hei):
    """
        This function builds the grid.
        Parameters:
            wid: Width of the grid
            hei: Height of the grid
        Returns:
            This function returns the south-west corner of the grid.
    """
    obj_grid = []
    floor_list = []
    for i in range(hei):
        for j in range(wid):
            floor_list.append(Grid())
        obj_grid.append(floor_list)
        floor_list = []
    sw_corner = populate_grid(wid, hei, obj_grid)
    return sw_corner
