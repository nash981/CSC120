#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on querying the
    most basic properties of a newly-created object.

    Author: Russ Lewis
"""

import connect_n_state



print("----- TEST 1 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(3,10, 9, ["Blue", "Green", "Mauve"])
print()

print("Dumping the basic properties:")
print(f"  get_size()       : {game.get_size()}")
print(f"  get_target()     : {game.get_target()}")
print(f"  get_player_list(): {game.get_player_list()}")
print()



print("----- TEST 2 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(3,3, 2, ["Red", "Yellow"])
print()

print("Dumping the basic properties:")
print(f"  get_size()       : {game.get_size()}")
print(f"  get_target()     : {game.get_target()}")
print(f"  get_player_list(): {game.get_player_list()}")
print()



print("----- TEST 3 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(6,7, 4, ["Yellow", "Red"])
print()

print("Dumping the basic properties:")
print(f"  get_size()       : {game.get_size()}")
print(f"  get_target()     : {game.get_target()}")
print(f"  get_player_list(): {game.get_player_list()}")
print()



print("----- TEST 4 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(10,10, 5, ["Red", "Yellow"])
print()

print("Dumping the basic properties:")
print(f"  get_size()       : {game.get_size()}")
print(f"  get_target()     : {game.get_target()}")
print(f"  get_player_list(): {game.get_player_list()}")
print()



print("TESTCASE COMPLETED")


