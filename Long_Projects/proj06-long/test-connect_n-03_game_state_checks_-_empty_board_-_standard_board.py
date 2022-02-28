#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on checking for
    game over conditions.

    Author: Russ Lewis
"""

import connect_n_state



print("Building the new object...")
game = connect_n_state.Connect_N_State(7,6, 4, ["Red", "Yellow"])
print()

print("Dumping the game state properties:")
print(f"  is_game_over()   : {game.is_game_over()}")
print(f"  is_board_full()  : {game.is_board_full()}")
print(f"  is_column_full(1): {game.is_column_full(1)}")
print(f"  is_column_full(2): {game.is_column_full(2)}")
print(f"  is_column_full(5): {game.is_column_full(5)}")
print()

print("TESTCASE COMPLETED")


