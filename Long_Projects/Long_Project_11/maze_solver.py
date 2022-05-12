"""
Author: Nishant Athawale
Date: 12th April 2022
Assignment: Long Project 11: Maze Solver
Class: CSC 120
Section Leader: Jason L'Italien
Section : #5
Description: This program aims to print all the palindromes in the set of
            words present in a given text file and their combinations
            upto a given word length.
By default (unless you tell a function to return something else),
all functions return None. None is actually a special type of object.
This is important because if None is a value, "returns nothing,"
"doesn't return anything," and "no returns" are incorrect.
"""
class Maze_Tree_node():
    """
        This class represents the node of a given postion in the maze.

        The class defines several helpful methods and fields:
        co_ordinates: Co-ordinates of valid path in the maze.
        val: content of concerned path place
        child_Dict: Dictionary mapping the directions with the
        respective child nodes.

        """
    def __init__(self, x_co_ordinate, y_co_ordinate, content):
        self.co_ordinates = (x_co_ordinate, y_co_ordinate)
        self.val = content
        self.child_Dict = {"top": None, "bottom": None, \
                           "right": None, "left": None}


def surrounding_check_parent(x, y, maze):
    """
    This function is specifically for the parent node and checks if the
    surrounding cells are part of a maze path
    Parameters:
        x: x_co-ordinate of the concerned cell
        y: y_co-ordinate of the concerned cell
        maze: The entire maze in a 2-D list format
    Returns:
        approval: A dictionary mapping directions to the following values:
                True: If the cell satisfies the path conditions
                False: If the cell does not satisfy the path conditions
    """
    approval = {"top": False, "bottom": False, "right": False, "left": False}
    # top
    if (y-1 >= 0) and (maze[x][y-1] == "#" or maze[x][y-1] == "E"):
        approval["top"] = True
    # bottom
    if (y+1 < len(maze)) and (maze[x][y+1] == "#" or maze[x][y+1] == "E"):
        approval["bottom"] = True
    # left
    if (x - 1 >= 0) and (maze[x - 1][y] == "#" or maze[x - 1][y] == "E"):
        approval["left"] = True
    # right
    if x+1 < len(maze[1]) and maze[x+1][y] == "#" or maze[x+1][y] == "E":
        approval["right"] = True

    return approval


def surrounding_check(x, y, maze, prev_x_node, prev_y_node):
    """
    This function is for all nodes apart from the parent node and
    checks if the surrounding cells are part of a maze path
    Parameters:
        x: x co-ordinate of the concerned cell
        y: y co-ordinate of the concerned cell
        maze: The entire maze in a 2-D list format
        prev_x_node: x co-ordinate of parent of the current node in the maze
        prev_y_node: y co-ordinate of parent of the current node in the maze
    Returns:
        approval: A dictionary mapping directions to the following values:
                True: If the cell satisfies the path conditions
                False: If the cell does not satisfy the path conditions
    """
    approval = {"top": False, "bottom": False, "right": False, "left": False}
    if (y-1 >= 0) and y-1 != prev_y_node and (maze[x][y-1] == "#" \
                                              or maze[x][y-1] == "E"):
        approval["top"] = True
    # bottom
    if (y+1 < len(maze)) and y+1 != prev_y_node and (maze[x][y+1] == "#" \
                                                     or maze[x][y+1] == "E"):
        approval["bottom"] = True
    # left
    if (x - 1 >= 0) and x - 1 != prev_x_node and (maze[x - 1][y] == "#" \
                                                  or maze[x - 1][y] == "E"):
        approval["left"] = True
    # right
    if x+1 < len(maze[1]) and x+1 != prev_x_node and maze[x+1][y] == "#" \
            or maze[x+1][y] == "E":
        approval["right"] = True

    return approval


def based(x, y, maze, prev_x_node = None, prev_y_node=None):
    """
    This function checks for the bases cases for the function tree_builder
    which recursively transforms the grid into a tree.
    Parameters:
        x: x co-ordinate of the concerned cell
        y: y co-ordinate of the concerned cell
        maze: The entire maze in a 2-D list format
        prev_x_node: x co-ordinate of parent of the current node in the maze
        prev_y_node: y co-ordinate of parent of the current node in the maze
    Returns:
        True: If Base case condition is satisfied
        False: If Base cases condition is not satisfied
    """
    surrounding_stats = {"top": False, "bottom": False, "right": False, \
                         "left": False}
    y_edge, x_edge = len(maze)-1, len(maze[1])-1
    if prev_x_node is None or prev_y_node is None:
        if x == 0 or maze[x-1][y] not in ["E","#"]:
            surrounding_stats["top"] = True
        if x == x_edge or maze[x+1][y] not in ["E","#"]:
            surrounding_stats["bottom"] = True
        if y == 0 or maze[x][y-1] not in ["E","#"] :
            surrounding_stats["left"] = True
        if y == y_edge or maze[x][y+1] not in ["E","#"]:
            surrounding_stats["right"] = True
    else:
        if x == 0 or x-1 != prev_x_node or maze[x-1][y] not in ["E","#"]:
            surrounding_stats["top"] = True
        if x == x_edge or x+1 != prev_x_node or maze[x+1][y] not in ["E","#"]:
            surrounding_stats["bottom"] = True
        if y == 0 or y-1 != prev_y_node or maze[x][y-1] not in ["E","#"] :
            surrounding_stats["left"] = True
        if y == y_edge or y+1 != prev_y_node or maze[x][y+1] not in ["E","#"]:
            surrounding_stats["right"] = True
    if (surrounding_stats["top"] and surrounding_stats["bottom"] and \
        surrounding_stats["left"] and surrounding_stats["right"]) is True:
        return True
    else:
        return False


def tree_builder(parent_node_index, maze, prev_x_node=None, prev_y_node=None):
    """
    This function recursively transforms a given maze into a tree with 4
    children based on directions.
    Parameters:
        parent_node_index: A tuple of x co-ordinate and y co-ordinate of
            the root node of the entire tree (co-ordinates of "S" in the
            given maze)
        maze: The entire maze in a 2-D list format
        prev_x_node: x co-ordinate of parent of the current node in the maze
        prev_y_node: y co-ordinate of parent of the current node in the maze
    Returns:
        parent_node: Root node of the tree

    """
    x = parent_node_index[0]
    y = parent_node_index[1]
    parent_node = Maze_Tree_node(x, y, maze[x][y])
    if based(x, y, maze, prev_x_node , prev_y_node) is True:
        return parent_node
    else:
        if prev_x_node is None or prev_y_node is None:
            approve = surrounding_check_parent(x, y, maze)
        else:
            approve = surrounding_check(x, y, maze, prev_x_node, prev_y_node)
        if approve["top"] is True:
            parent_node.child_Dict["top"] = \
                tree_builder((x, y-1), maze, x, y)
        if approve["bottom"] is True:
            parent_node.child_Dict["bottom"] = \
                tree_builder((x, y+1), maze, x, y)
        if approve["left"] is True:
            parent_node.child_Dict["left"] = \
                tree_builder((x - 1, y), maze, x, y)
        if approve["right"] is True:
            parent_node.child_Dict["right"] =\
                tree_builder((x + 1, y), maze, x, y)
        return parent_node


def maze_builder(filename):
    """
    This function gives processes the given text file representing the
    maze into a 2-D array.
    Parameters:
        filename: Name of the file to be read
    Returns:
        maze: The entire maze in a 2-D list format
    Error:
        This function prints a message to inform the user that file
        does not exist. Then the program is terminated.
    """
    try:
        text = open(filename, "r")
        maze = []
        for lines in text:
            temp = []
            for chars in lines:
                temp.append(chars)
            maze.append(temp)
        if len(maze[-1]) != len(maze[-2]):
            for i in range(abs(len(maze[-1])-len(maze[-2]))):
                maze[-1].append(" ")
        text.close()
        return maze
    except FileNotFoundError or FileExistsError:
        print("ERROR: Could not open file: NO_SUCH_FILE")
        exit()


def count_specs(maze):
    """
    This function counts the occurrences of "E" and "S" in the given maze.
    Parameters:
        maze: The entire maze in a 2-D list format
    Returns:
        e_count: Number of occurrences of  "E"
        s_count: Number of occurrences of  "S"
    """
    e_count, s_count = 0, 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                s_count += 1
            if maze[i][j] == "E":
                e_count += 1
    return e_count, s_count


def condition_check(maze):
    """
    This function checks the maze for possible invalid conditions
    Parameters:
        maze: The entire maze in a 2-D list format
    Returns: None

    Errors:
        Invalid characters
        Exactly one occurrence of "E" and "S"
        If any of these errors occur, this function print the appropriate
        error messages and then exits the program.

    """
    e_count, s_count = count_specs(maze)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] in ["S", "E", "#", " ", "\n"]:
                if maze[i][j] != " ":
                    continue
            else:
                print("ERROR: Invalid character in the map")
                quit()
    if s_count > 1:
        print("ERROR: The map has more than one START position")
        quit()
    elif s_count == 0:
        print("ERROR: Every map needs exactly one START and exactly" \
              + "one END position")
        quit()
    elif e_count > 1:
        print("ERROR: The map has more than one END position")
        quit()
    elif e_count == 0:
        print("ERROR: Every map needs exactly one START and exactly" \
              + "one END position")
        quit()


def dump_vals(maze):
    """
    This function  prints all appropriate maze cells
    Parameters:
        maze: The entire maze in a 2-D list format
    Returns: None
    """
    path_list = []
    print("DUMPING OUT ALL CELLS FROM THE MAZE:")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] in ["S", "E", "#", " ", "\n"]:
                if maze[i][j] != " ":
                    path_list.append((j, i))
    path_list.sort()
    for i in range(len(path_list)):
        if maze[path_list[i][1]][path_list[i][0]] == "#":
            print(f"  {path_list[i]}")
        elif maze[path_list[i][1]][path_list[i][0]] == "S":
            print(f"  {path_list[i]}    START")
        elif maze[path_list[i][1]][path_list[i][0]] == "E":
            print(f"  {path_list[i]}    END")


def command_check(command):
    """
    This function checks the validity of commands.
    Parameters:
        command: The command string
    Returns: None

    Error:
        If the command is invalid, the function prints the appropriate error
        message and exits the program.
    """
    if command == "dumpSolution" or command == "dumpSize" or\
            command == "dumpTree" or command == "dumpCells" or command == "":
        return None
    else:
        print("ERROR: Unrecognized command NOT_A_VALID_COMMAND")
        quit()


def parent_index(maze):
    """
    This function finds the index of the postion where
    "S" is the value in the maze (root_node)
    Parameters:
        maze: The entire maze in a 2-D list format
    Returns:
        A tuple containing x and y co-ordinates of the concerned
        position in the maze.
    """
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return ((i,j))


def print_tree(parent_node, prev_string="  "):
    """
    This function prints the entire tree, one child at a time
    Parameters:
        parent_node: Root node of the tree
        prev_string: The string to keep track of the tree levels
    Returns: None
    """
    print(f"{prev_string} {parent_node.co_ordinates}")
    pass_on_string = f"{prev_string} |"
    if parent_node.child_Dict["top"] is None and \
        parent_node.child_Dict["bottom"] is None and \
            parent_node.child_Dict["left"] is None and \
            parent_node.child_Dict["right"] is None:
        return None
    if parent_node.child_Dict["top"] is not None:
        print_tree(parent_node.child_Dict["top"], pass_on_string)
    if parent_node.child_Dict["bottom"] is not None:
        print_tree(parent_node.child_Dict["bottom"], pass_on_string)
    if parent_node.child_Dict["left"] is not None:
        print_tree(parent_node.child_Dict["left"], pass_on_string)
    if parent_node.child_Dict["right"] is not None:
        print_tree(parent_node.child_Dict["right"], pass_on_string)


def main():
    """
    This function runs the entire program.
    """
    filename = input()
    maze = maze_builder(filename)
    condition_check(maze)
    parent_node_index = parent_index(maze)
    #parent_node = tree_builder(parent_node_index, maze)
    #print_tree(parent_node)
    command = input()
    command_check(command)
    if command.lower() == "dumpcells":
        dump_vals(maze)


if __name__ == '__main__':
    main()
