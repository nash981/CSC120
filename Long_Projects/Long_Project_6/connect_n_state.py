"""
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
"""


def grid_build(wid, hei):
    """
    This function builds and returns a 2 Dimensional list with
    value of each element being "."
    Parameters:
        wid: Width of the Grid
        hei: Height of the Grid
    Returns:
        grid: A grid with each element as "."
    """
    grid = []
    floor_list = []
    for i in range(hei):
        for j in range(wid):
            floor_list.append(".")
        grid.append(floor_list)
        floor_list = []
    return grid


def transpose(in_list):
    """
    This function converts the list from x-y form to y-x form.
    This function helps in traversing the original list vertically.
    Parameters:
        in_list: The original list
    Returns:
        out_list: The transformed list
    """
    out_list = []
    for i in range(len(in_list[0])):
        row = []
        for item in in_list:
            row.append(item[i])
        out_list.append(row)
    return out_list


class Connect_N_State:
    """
    This class represents the current state of  Connect-N game.

    The constructor initialized the fields of the class with
    the list of players, the target size, the height and the width
    of the grid. The constructor also initialized a field by building
    a grid of "." which shows the state of the Connect-N grid.

    The class defines several helpful methods and fields:
        width:          Width of the game grid
        height:         Height of the game grid
        playah:         List of players in the game.
        grid:           The grid storing the status of the game
        count:          Counts the number of turns
        curr_playah:    Stores the player whose turn has just ended
        playah_dict:    Maps the first letter of every player name
                        to the player name
        get_size():     Getter function for the dimensions of the game grid.
        map_players():  Maps the first letter of every player name
                        to the player name
        get_target():   Getter function for the target length
        get_player_list():  Getter function for the list of players
        get_cell():     Getter function for the contents at a given cell of
                        the grid.
        is_column_full():   Checks if a given column is full
        is_board_full():    Checks if the entire board/grid is full
        lateral_words():    Extracts words in linear directions
        lateral_search():   Checks if the target length is achieved by a
                            player in linear direction.
        diagonal_words():   Extracts words in diagonal directions
        diagonal_search():  Checks if the target length is achieved by a
                            player in diagonal direction.
        board_check():  Checks if target length is achieved in both linear
                        and diagonal directions.
        is_game_over(): Checks if the game is over by checking if the target
                        length is achieved or if the board is full.
        get_winner():   Returns the game winner
        get_cur_player():   Returns the player whose turn is next.
        move():         Executes the game moves
        print():        Prints the grid/board.
    """
    def __init__(self, wid, hei, target, players):
        self._width = wid
        self._height = hei
        self._target = target
        self._playah = players
        self._grid = grid_build(wid, hei)
        self._count = 0
        self._curr_playah = None
        self._playah_dict = self.map_players()

    def get_size(self):
        """
        This funtion returns the dimensions of the grid/ board
        Parameters:
            self:   This refers to the object itself

        Returns:
            x:  The tuple containing the width and height of the
                grid/board.
        """
        x = (self._width, self._height)
        return x

    def map_players(self):
        """
        This function maps the player names the first letter of their
        name.
        Parameters:
            self:   This refers to the object itself
        Returns:
            out_dict: The dictionary containing the mappings.
        """
        out_dict = {}
        for i in range(len(self._playah)):
            out_dict[self._playah[i][0]] = self._playah[i]
        return out_dict

    def get_target(self):
        """
        This function returns the target length of the game
        Parameters:
            self:   This refers to the object itself
        Returns:
            target: The desired length to win the game
        """
        target = self._target
        return target

    def get_player_list(self):
        """
        This function returns the player list
        Parameters:
            self:   This refers to the object itself
        Returns:
            The field containing the list of players.
        """
        return self._playah

    def get_cell(self, x, y):
        """
        This function returns the token in a given
        place in the grid (if any).
        Parameters:
            self:   This refers to the object itself
            x:  The co-ordinate on the vertical axis.
            y:  The co-ordinate on the horizontal axis.
        Returns:
            The contents of the slot on the grid
            None:   If the position contains a "."

        """
        if self._grid[y][x] != ".":
            return self._playah_dict[self._grid[y][x]]

    def is_column_full(self, col):
        """
        Checks if a given column is full
        Parameters:
            self:   This refers to the object itself
            col:    The index of the column which is to be checked
        Returns:
            True:   If the column is full
            False: If the column is not full.
        """
        for i in range(self._height):
            if self._grid[i][col] == ".":
                return False
        return True

    def is_board_full(self):
        """
        Checks if the entire board is full with tokens
        Parameters:
            self:   This refers to the object itself
        Returns:
            True:   If the board is full
            False:  If the board is not full.

        """
        for i in range(self._height):
            for j in range(self._width):
                if self._grid[i][j] == ".":
                    return False
        return True

    def lateral_words(self, i, j, transpose_list):
        """
        This function extracts the words in linear directions
        Parameters:
            self:   This refers to the object itself
            i:      The vertical index
            j:      The horizontal index
            transpose_list: The transformed list used for traversing in
                            vertical direction.
        Returns:
            word_list:  A list of characters in all 4 linear directions.
        """
        word_list = [[], [], [], []]
        if i-self._target >= 0:
            word_list[0] = transpose_list[j][i-self._target+1:i+1]
        if i+self._target <= self._height:
            word_list[1] = transpose_list[j][i:i+self._target]
        if j+self._target <= self._width:
            word_list[2] = self._grid[i][j:j+self._target]
        if j-self._target >= 0:
            word_list[3] = self._grid[i][j-self._target+1:j+1]
        return word_list

    def lateral_search(self, x, y):
        """
        This function checks if the target length is achieved in the
        linear direction
        Parameters:
            self:   This refers to the object itself
            x:      The vertical index
            y:      The horizontal index
        Returns:
            True:   If the target length is achieved
            False:  If the target length is not achieved.
        """
        stat, status = [], True
        transposed_list = transpose(self._grid)
        words = self.lateral_words(x, y, transposed_list)
        for item in words:
            if len(item) == self._target and "." not in item:
                for j in range(self._target-1):
                    if item[j] != item[j+1]:
                        status = False
                if status is True:
                    stat.append(True)
            else:
                stat.append(False)
        if True in stat:
            return True
        else:
            return False

    def diagonal_words(self, x, y):
        """
        This function extracts the words in diagonal directions
        Parameters:
            self:   This refers to the object itself
            x:      The vertical index
            y:      The horizontal index
        Returns:
            word_list:  A list of characters in all 4 diagonal directions.
        """
        word_list = [[], [], [], []]
        for i in range(self._target):
            if x - self._target >= 0 and y-self._target >= 0:
                word_list[0].append(self._grid[x-i][y-i])
            if x - self._target >= 0 and y+self._target <= self._width:
                word_list[1].append(self._grid[x-i][y+i])
            if x + self._target <= self._height and y-self._target >= 0:
                word_list[3].append(self._grid[x+i][y-i])
            if x + self._target <= self._height and \
                    y+self._target <= self._width:
                word_list[2].append(self._grid[x+i][y+i])
        return word_list

    def diagonal_search(self, x, y):
        """
        This function checks if the target length is achieved in the
        diagonal direction
        Parameters:
            self:   This refers to the object itself
            x:      The vertical index
            y:      The horizontal index
        Returns:
            True:   If the target length is achieved
            False:  If the target length is not achieved.
        """
        stat, status = [], True
        words = self.diagonal_words(x, y)
        for item in words:
            if len(item) == self._target and "." not in item:
                for j in range(self._target-1):
                    if item[j] != item[j+1]:
                        status = False
                if status is True:
                    stat.append(True)
            else:
                stat.append(False)
        if True in stat:
            return True
        else:
            return False

    def board_check(self):
        """
        This function checks if the target length is achieved in the
        linear or diagonal direction
        Parameters:
            self:   This refers to the object itself
        Returns:
             True:   If the target length is achieved
             False:  If the target length is not achieved.
        """
        for i in range(self._height):
            for j in range(self._width):
                lateral_status = self.lateral_search(i, j)
                diagonal_status = self.diagonal_search(i, j)
                if lateral_status is True or diagonal_status is True:
                    return True
        return False

    def is_game_over(self):
        """
        Checks the game over condtions
        Parameters:
            self:   This refers to the object itself
        Returns:
             True:  If the target length is achieved or if the board is full
             False: If the target length is not achieved and
                    board is not full.
        """
        board_stat = self.board_check()
        board_full = self.is_board_full()
        if board_stat is True or board_full is True:
            return True
        else:
            return False

    def get_winner(self):
        """
        This function returns the winner of the game.
        Parameters:
            self:   This refers to the object itself
        Returns:
            The winner of the game

        """
        return self._curr_playah

    def get_cur_player(self):
        """
        This function returns the next player
        Parameters:
            self:   This refers to the object itself
        Returns:
            The next player
        """
        player_count = len(self._playah)
        player_index = self._count % player_count
        return self._playah[player_index]

    def move(self, col):
        """
        This function executes the move by adding appropriate token
        in the desired column
        Parameters:
            self:   This refers to the object itself
            col:    Column in which the token is to be added.
        Returns:
            True:   If the move is successful
            False:  If the move fails
        """
        self._curr_playah = self.get_cur_player()
        for i in range(self._height):
            if self._grid[i][col] == ".":
                self._grid[i][col] = self._curr_playah[0]
                self._count += 1
                return True
        return False

    def print(self):
        """
        This function prints the status of the board
        when this function is called.
        Parameters:
            self:   This refers to the object itself
        Returns: None
        """
        out_str = ""
        self._grid.reverse()
        for i in range(self._height):
            for j in range(self._width):
                out_str += self._grid[i][j]
            print(out_str)
            out_str = ""
        self._grid.reverse()
