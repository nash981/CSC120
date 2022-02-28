#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on checking to
    see if the get_cell() call works properly.

    Author: Russ Lewis
"""

import connect_n_state



print("Building the new object...")
game = connect_n_state.Connect_N_State(7,6, 4, ["Red", "Yellow"])
print()

print("Doing a few get_cell() calls:")
print(f"  (0,0) : {game.get_cell(0,0)}")
print(f"  (2,0) : {game.get_cell(2,0)}")
print(f"  (4,2) : {game.get_cell(4,2)}")
print(f"  (4,5) : {game.get_cell(4,5)}")
print(f"  (6,3) : {game.get_cell(6,3)}")
print(f"  (0,5) : {game.get_cell(0,5)}")
print()

print("TESTCASE COMPLETED")


