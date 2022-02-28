#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on querying the
    most basic properties of a newly-created object.

    Author: Russ Lewis
"""

import connect_n_state



print("Building the new object...")
game = connect_n_state.Connect_N_State(7,6, 4, ["Red", "Yellow"])
print()

print("Dumping the basic properties:")
print(f"  get_size()       : {game.get_size()}")
print(f"  get_target()     : {game.get_target()}")
print(f"  get_player_list(): {game.get_player_list()}")
print()

print("TESTCASE COMPLETED")


