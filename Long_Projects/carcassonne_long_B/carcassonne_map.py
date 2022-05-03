"""
Author: Nishant Athawale
Date: 19th April 2022
Assignment: Carcassonne Long A
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: This program builds a class representing a Carcassonne Map
                defines a few methods to run the game.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""
from carcassonne_tile import *

class CarcassonneMap:
    """
    This class represents the map of a particular Carcassonne game.
    This Class contains following fields:
    map: this field stores the game state in form of a dictionary by
        mapping a tuple containing the x and y co-ordinate of a given
        tile on the map to its respective tile.
    This class contains the following class methods:
        get_all_coords
        find_map_border()   : This function returns a list of all possible
                                places where a new tile can be inserted
        get()               : This function returns a tile at desired location
        surrounding_tiles() : This function returns a dictionary containing
                                all the tiles present on the map and surround
                                the desired insertion index.
        error_check()       : This function checks for all the conditions
                                required to successfully insert a tile in
                                a given postion.
        add()               : This function inserts a given tile in a given
                                position in the map.


    """
    def __init__(self):
        """
        This constructor initializes a new Map object with a map field
         containing a tile coded as tile01 at the postion x = 0 and y = 0
        Parameters:
            self: The tile object itself
        Returns: None
        """
        self._map = {(0, 0): tile01}
        self.offset_dict = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        self.side_dict = {0: 2, 2: 0, 1: 3, 3: 1}

    def get_all_coords(self):
        """
        This function returns a set of co-ordinate tuples of all
         the tiles present on the carcassonne map.
        Parameters:
            self: The tile object itself
        Returns:
            output_keys: A set of all co-ordinate tuples
        """
        output_keys = set()
        for keys in self._map:
            output_keys.add(keys)
        return output_keys

    def find_map_border(self):
        """
        This function finds the all the possible empty locations adjacent
         to the existing tiles on the map.
        Parameters:
            self: The tile object itself
        Returns:
            border_co_ordinates: A set of all co-ordinate tuples of all empty
                                positions on the carcassonne map that are
                                adjacent to existing postions on the map.
        """
        border_co_ordinates = set()
        for keys in self._map:
            if (keys[0]+1, keys[1]) not in self._map.keys():
                border_co_ordinates.add((keys[0]+1, keys[1]))
            if (keys[0]-1, keys[1]) not in self._map.keys():
                border_co_ordinates.add((keys[0]-1, keys[1]))
            if (keys[0], keys[1]+1) not in self._map.keys():
                border_co_ordinates.add((keys[0], keys[1]+1))
            if (keys[0], keys[1]-1) not in self._map.keys():
                border_co_ordinates.add((keys[0], keys[1]-1))
        return border_co_ordinates

    def get(self, x, y):
        """

        Parameters:
            self: The tile object itself
        Returns:
        """
        if (x, y) in self._map.keys():
            return self._map[(x, y)]
        else:
            return None

    def surrounding_tiles(self, x, y):
        """
            This function finds all the tiles surrounding the desired empty
            positions that are present on the carcassonne map.
        Parameters:
            self: The tile object itself
            x: x co-ordinate of the insertion postion
            y: y co-ordinate of the insertion postion
        Returns:
            nearby_coods : Dictionary of nearby existing postions in the
                            map with key as the position tuple and all values
                            initialized ot False.
        """
        nearby_coods = {}
        if (x - 1, y) in self._map:
            nearby_coods[(x - 1, y)] = False
        if (x + 1, y) in self._map:
            nearby_coods[(x + 1, y)] = False
        if (x, y - 1) in self._map:
            nearby_coods[(x, y - 1)] = False
        if (x, y + 1) in self._map:
            nearby_coods[(x, y + 1)] = False
        return nearby_coods

    def error_check(self, x, y, tile):
        """
        This function checks for all the error conditions that are
        specified in the spec sheet.
        Parameters:
            self:   The tile object itself
            x:      x co-ordinate of the insertion position
            y:      y co-ordinate of the insertion position
            tile:   The tile to be inserted
        Returns:
            True:   If all conditions are satisfied
            False:  If atleast one condition is not satisfied.
        """
        nearby_coods = self.surrounding_tiles(x, y)
        border_cood = self.find_map_border()
        if x == 0 and y == 0:
            return False, True
        elif nearby_coods == {}:
            return False, False
        elif (x, y) in border_cood:
            if (x - 1, y) in nearby_coods and tile.West == \
                    self._map[(x - 1, y)].East:
                nearby_coods[(x - 1, y)] = True
            if (x + 1, y) in nearby_coods and tile.East == \
                    self._map[(x + 1, y)].West:
                nearby_coods[(x + 1, y)] = True
            if (x, y - 1) in nearby_coods and tile.South == \
                    self._map[(x, y - 1)].North:
                nearby_coods[(x, y - 1)] = True
            if (x, y + 1) in nearby_coods and tile.North == \
                    self._map[(x, y + 1)].South:
                nearby_coods[(x, y + 1)] = True
        if False in nearby_coods.values():
            return False, False
        else:
            return True, False

    def add(self, x, y, tile, confirm=True, tryOnly=False):
        """
        This function inserts a given tile in the map at given
         postion provided all conditions are satisfied
        Parameters:
            self:    The tile object itself.
            x:       x co-ordinate of the insertion position.
            y:       y co-ordinate of the insertion position.
            tile:    The tile to be inserted.
            confirm: Enables or Disables error checking.
            tryOnly: Enables or Disables insertion.
        Returns:
            True: If tile is / can be inserted in the given position
            False: If tile is / can be not inserted in the given position.
        """
        error_check, origin_check = self.error_check(x,y,tile)
        if (x, y) not in self._map and origin_check is False:
            if confirm is True and tryOnly is False:
                if error_check is True:
                    self._map[(x,y)] = tile
                return error_check
            elif confirm is True and tryOnly is True:
                return error_check
            elif confirm is False and tryOnly is False:
                self._map[(x, y)] = tile
                return True
        else:
            if confirm is False and tryOnly is False:
                self._map[(x, y)] = tile
                return True
            return False

    def recurse(self, x, y, side, og_posn):
        next_side = self._map[(x,y)].road_get_connection(side)
        output = [(x, y, side, next_side)]
        if next_side != -1 and (x, y, next_side) != og_posn:
            offsets = self.offset_dict[next_side]
            x_next, y_next = x + offsets[0], y + offsets[1]
            if (x_next, y_next) in self._map:
                output += self.recurse(x_next, y_next,
                                       self.side_dict[next_side], og_posn)
        return output

    def trace_road_one_direction(self, x, y, side):
        if side != -1:
            offsets = self.offset_dict[side]
            x_next, y_next = x+offsets[0], y+offsets[1]
            if (x_next,y_next) in self._map:
                og_posn = (x, y, side)
                output = self.recurse(x_next, y_next,
                                      self.side_dict[side], og_posn)
                return output
        return []

    def recurse_reversed(self, x, y, side, og_posn):
        next_side = self._map[(x,y)].road_get_connection(side)
        output = [(x, y, next_side, side)]
        if next_side != -1 and (x, y, next_side) != og_posn:
            offsets = self.offset_dict[next_side]
            x_next, y_next = x + offsets[0], y + offsets[1]
            if (x_next, y_next) in self._map:
                output = self.recurse_reversed(x_next, y_next,
                                      self.side_dict[next_side], og_posn)\
                         + output

        return output

    def trace_road_one_direction_reversed(self, x, y, side):
        if side != -1:
            offsets = self.offset_dict[side]
            x_next, y_next = x+offsets[0], y+offsets[1]
            if (x_next,y_next) in self._map:
                og_posn = (x, y, side)
                output = self.recurse_reversed(x_next, y_next,
                                      self.side_dict[side], og_posn)
                return output
        return []

    def trace_road(self, x, y, side):
        other_side = self._map[(x,y)].road_get_connection(side)
        if other_side != -1:
            passed_side = self.trace_road_one_direction(x, y, side)
            curr_tile = [(x, y, other_side, side)]
            second_side = self.trace_road_one_direction_reversed(x, y, other_side)
            if passed_side[:-1] != second_side[1:]:
                output_list = second_side + curr_tile + passed_side
            else:
                output_list = second_side[1:] + curr_tile
            return output_list
        else:


