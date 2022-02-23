'''
    Author: Nishant Athawale
    Date: 22nd February 2022
    Class: CSC 120
    Section Leader: Jason L'Italien
    Section : #5
    Description:
    This is aimed to practice classes.

    By default (unless you tell a function to return something else),
    all functions return None. None is actually a special type of object.
    This is important because if None is a value, "returns nothing,"
    "doesn't return anything," and "no returns" are incorrect.
'''


def set_val(val):
    '''
        This function sets the value of input argument
        in the range from 0 to 255.
        Parameter:
        val: Input value from the user
        Returns:
            0: If the value is negative
            255: If value is greater than 255
            val: If the value is between 0 and 255
    '''
    if val < 0:
        return 0
    elif val > 255:
        return 255
    else:
        return val


class Color:
    """
           This class represents a color in its RGB values.
           The r, g and b values must be passed by the user
           while initializing the object.

           The class defines several helpful methods and fields:
               html_hex_color(): This function converts the
               r, g and b values from decimal values and converts
               it into a hex representation of colors.
               get_rgb() : Getter function for r, g and b values.
               set_standard_color(): Sets RGB values for given
               color.
               remove_red(): Set the r value of object to 0.

          """
    def __init__(self, r, g, b):
        self._r = set_val(r)
        self._g = set_val(g)
        self._b = set_val(b)

    def __str__(self):
        _string = f"rgb({self._r},{self._g},{self._b})"
        return _string

    def html_hex_color(self):
        '''
            This function converts the
            r, g and b values from decimal values and converts
            it into a hex representation of colors.
            Parameters:
                self:   This refers to the object itself
            Returns:
                A string giving the hex representation
                of a color
        '''
        _hex_r = hex(self._r)
        _hex_g = hex(self._g)
        _hex_b = hex(self._b)
        if len(_hex_r) != 4:
            _hex_red = "0"
            _hex_red += _hex_r[-1]
        else:
            _hex_red = _hex_r[-2:]
        if len(_hex_g) != 4:
            _hex_green = "0"
            _hex_green += _hex_g[-1]
        else:
            _hex_green = _hex_g[-2:]
        if len(_hex_b) != 4:
            _hex_blue = "0"
            _hex_blue += _hex_b[-1]
        else:
            _hex_blue = _hex_b[-2:]

        _string = f"#{_hex_red}{_hex_green}{_hex_blue}".upper()
        return _string

    def get_rgb(self):
        '''
            This function returns RGB values of the object
            Parameters:
                 self:   This refers to the object itself
            Returns:
                _r: R value
                _g: G value
                _b: B value
        '''
        _x = (self._r, self._g, self._b)
        return _x

    def set_standard_color(self, name):
        '''
            This function Sets RGB values for given color.
            Parameters:
                self:   This refers to the object itself
            Returns: None
        '''
        _name = name.lower()
        if _name == "white":
            self._r = 255
            self._g = 255
            self._b = 255
        elif _name == "red":
            self._r = 255
            self._g = 0
            self._b = 0
        elif _name == "yellow":
            self._r = 255
            self._g = 255
            self._b = 0
        elif _name == "black":
            self._r = 0
            self._g = 0
            self._b = 0

    def remove_red(self):
        '''
            This function sets r value to zero
            Parameters:
                self:   This refers to the object itself
            Returns: None
        '''
        self._r = 0
