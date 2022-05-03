"""
Author: Nishant Athawale
Date: 19th April 2022
Assignment: Carcassonne Short A
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: This program builds a class representing a general carcassonne
                tile and defines a few class methods to process a given tile.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""


class CarcassonneTile:
    """
            This class represents a carcassonne tile.
            This class contains the following fields:
            North:  Holds the object in the North direction of the tile
            South:  Holds the object in the South direction of the tile
            East:   Holds the object in the East direction of the tile
            West:   Holds the object in the West direction of the tile
            Centre: Holds the object at the Centre of the tile
            Reference: A list of containing North, East, South and West fields.

            The constructor builds a general carcassonne tile with each of the
            location fields containing one of the following objects:
            grass
            city
            grass+road
            crossroad

           The class defines several helpful methods and fields:
               get_edge()           :Returns value stored at a particular edge
                                        of the tile.
               edge_has_road()      : Checks if any edge of the tile has an
                                        edge
               edge_has_city()      : Checks if any edge of the tile has a city
               has_crossroads()     : Checks if a given tile has a crossroad
               road_get_connection(): Checks the connections of the roads
               city_connects()      : Checks of cities are connected in a
                                        given tile
               rotate()             : Rotates a given tile 90 degrees
                                        clockwise.
        """
    def __init__(self, North, East, South, West, Centre = None):
        """
        This constructor function initializes the member fields with
        user defined values
        Parameters:
            self: The tile object itself
            North:  The object stored in North direction
            East:   The object stored in East direction
            South:  The object stored in South direction
            West:   The object stored in West direction
            Centre: The object stored at Center. If not specified by the user
                    this field is assigned a default value of None
        Returns: None
        """
        self.North = North
        self.East = East
        self.South = South
        self.West = West
        self.Centre = Centre
        self.Reference = [self.North, self.East, self.South, self.West]

    def get_edge(self, side):
        """
        This function returns the object stored in the location fields of
        the class.
        Parameters:
            self: The tile object itself
            side: An integer specifying the required side
                    0:  North
                    1:  East
                    2:  South
                    3:  West
        Returns :
            Location field requested by the user.

        """
        if side == 0:
            return self.North
        elif side == 1:
            return self.East
        elif side == 2:
            return self.South
        elif side == 3:
            return self.West

    def edge_has_road(self, side):
        """
        This function checks if the desired edges of the current tile
        have roads or not.
        Parameters:
            self: The tile object itself
            side: An integer specifying the required side
                    0:  North
                    1:  East
                    2:  South
                    3:  West
        Returns:
            True: If any of the desired edges have a road
            False: If otherwise

        """
        if (side == 0 and self.North == "grass+road") or \
                (side == 1 and self.East == "grass+road") or \
                (side == 2 and self.South == "grass+road") or \
                (side == 3 and self.West == "grass+road"):
            return True
        else:
            return False

    def edge_has_city(self, side):
        """
                This function checks if the desired edges of the current tile
                have a city or not.
                Parameters:
                    self: The tile object itself
                    side: An integer specifying the required side
                            0:  North
                            1:  East
                            2:  South
                            3:  West
                Returns:
                    True: If any of the desired edges have a city
                    False: If otherwise

                """
        if (side == 0 and self.North == "city") or \
                (side == 1 and self.East == "city") or \
                (side == 2 and self.South == "city") or \
                (side == 3 and self.West == "city"):
            return True
        else:
            return False

    def has_crossroads(self):
        """
           This function checks if the tile has a crossroad at its centre
           Parameters:
               self: The tile object itself
           Returns:
               True: If any of the tile has a crossraod at its center
               False: If otherwise

           """
        if self.Centre == "crossroad":
            return True
        else:
            return False

    def road_get_connection(self, from_side):
        """
        This function returns the side that a given road is connected to.
        Parameters:
            self: The tile object itself
            from_side: The side to which we have to check road connections
        Returns:
                -1: If given road connected to a crossroad
                0:  If given road connected to a road in North direction
                1:  If given road connected to a road in East direction
                2:  If given road connected to a road in South direction
                3:   If given road connected to a road in West direction

        """
        if self.Centre == "crossroad":
            return -1
        elif self.Centre == "grass+road":
            if self.North == "grass+road" and from_side != 0:
                return 0
            elif self.East == "grass+road" and from_side != 1:
                return 1
            elif self.South == "grass+road" and from_side != 2:
                return 2
            elif self.West == "grass+road" and from_side != 3:
                return 3

    def city_connects(self, sideA, sideB):
        """
        Checks whether or not the two sides are both cities and they are
        connected.
        Parameters:
            self:   The tile object itself
            sideA:  First position
            sideB:  Second postion
        Returns:
            True: If the two sides are both cities, and they are connected.
            False: If otherwise
        """
        if self.Centre == "city" or self.Centre == "grass+road":
            if self.Reference[sideA] == self.Reference[sideB]:
                return True
        elif sideA == sideB:
            return True
        return False

    def rotate(self):
        """
        This function rotates the existing tile object by passing the
        location fields to create a new rotated tile object.
        Parameters:
            self:   The tile object itself
        Returns:
            new_tile: A new tile object containing the rotated tile.
        """
        new_tile = CarcassonneTile(self.West, self.North, self.East,
                                   self.South, self.Centre)
        return new_tile


# The following lines of code define some commonly used tiles in the \
# Carcassonne game


tile01 = CarcassonneTile("city", "grass+road", "grass", "grass+road",
                         "grass+road")
tile02 = CarcassonneTile("city", "city", "grass", "city", "city")
tile03 = CarcassonneTile("grass+road", "grass+road", "grass+road",
                         "grass+road", "crossroad")
tile04 = CarcassonneTile("city", "grass+road", "grass+road", "grass",
                         "grass+road")
tile05 = CarcassonneTile("city", "city", "city", "city", "city")
tile06 = CarcassonneTile("grass+road", "grass", "grass+road", "grass",
                         "grass+road")
tile07 = CarcassonneTile("grass", "city", "grass", "city", "grass")
tile08 = CarcassonneTile("grass", "city", "grass", "city", "city")
tile09 = CarcassonneTile("city", "city", "grass", "grass", "city")
tile10 = CarcassonneTile("grass", "grass+road", "grass+road", "grass+road",
                         "crossroad")
tile11 = CarcassonneTile("city", "grass+road", "grass+road", "city",
                         "grass+road")
tile12 = CarcassonneTile("city", "grass", "grass+road", "grass+road",
                         "grass+road")
tile13 = CarcassonneTile("city", "grass+road", "grass+road", "grass+road",
                         "crossroad")
tile14 = CarcassonneTile("city", "city", "grass", "grass", "grass")
tile15 = CarcassonneTile("grass", "grass", "grass+road", "grass+road",
                         "grass+road")
tile16 = CarcassonneTile("city", "grass", "grass", "grass", "grass")
