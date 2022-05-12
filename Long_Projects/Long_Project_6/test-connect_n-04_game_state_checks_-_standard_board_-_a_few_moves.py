#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on checking for
    game over conditions.

    Author: Russ Lewis
"""

import connect_n_state



print("Building the new object...")
game = connect_n_state.Connect_N_State(7,6, 4, ["Red", "Yellow"])
print()

print("Playing a few moves...")
if not game.move(1) or not game.move(0) or not game.move(2) or not game.move(3) or \
   not game.move(3) or not game.move(3) or not game.move(3) or not game.move(4) or \
   not game.move(6) or not game.move(1) or not game.move(2):
      print("ERROR: One or more of the moves was rejected.")
print()




print("Dumping the game state properties:")
print(f"  is_game_over()   : {game.is_game_over()}")
print(f"  is_board_full()  : {game.is_board_full()}")
print(f"  is_column_full(0): {game.is_column_full(0)}")
print(f"  is_column_full(1): {game.is_column_full(1)}")
print(f"  is_column_full(2): {game.is_column_full(2)}")
print(f"  is_column_full(3): {game.is_column_full(3)}")
print(f"  is_column_full(4): {game.is_column_full(4)}")
print(f"  is_column_full(5): {game.is_column_full(5)}")
print(f"  is_column_full(6): {game.is_column_full(6)}")
print()

print("TESTCASE COMPLETED")


