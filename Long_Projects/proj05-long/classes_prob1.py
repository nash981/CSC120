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
class Simplest:
    """
           This class take three values and assigns them
           to field a,b and c

          """
    def __init__(self, p, q, r):
        self.a = p
        self.b = q
        self.c = r


class Rotate:

    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third

    def rotate(self):
        temp = self._first
        self._first = self._second
        self._second = self._third
        self._third = temp


class Band:
    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitar = []

    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_drummer(self):
        return self._drummer

    def set_drummer(self, new_drummer):
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self._guitar.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self._guitar = []

    def get_guitar_players(self):
        out_list = []
        for i in range(len(self._guitar)):
            out_list.append(self._guitar[i])
        return out_list

    def play_music(self):
        if self._singer == "Frank Sinatra":
            print("Do be do be do")
        elif self._singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if self._drummer is not None:
            print("Bang bang bang!")
        if len(self._guitar) >0:
            for i in range(len(self._guitar)):
                print("Strum!")


