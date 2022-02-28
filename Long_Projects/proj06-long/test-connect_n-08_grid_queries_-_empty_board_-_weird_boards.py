#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on checking to
    see if the get_cell() call works properly.

    Author: Russ Lewis
"""

import connect_n_state



print("----- TEST 1 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(3,10, 9, ["Blue", "Green", "Mauve"])
print()

print(f"  (1,9) : {game.get_cell(1,9)}")
print(f"  (1,7) : {game.get_cell(1,7)}")
print(f"  (0,4) : {game.get_cell(0,4)}")
print(f"  (2,6) : {game.get_cell(2,6)}")
print(f"  (1,3) : {game.get_cell(1,3)}")
print(f"  (2,3) : {game.get_cell(2,3)}")
print()



print("----- TEST 2 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(3,3, 2, ["Red", "Yellow"])
print()

print(f"  (2,0) : {game.get_cell(2,0)}")
print(f"  (1,0) : {game.get_cell(1,0)}")
print(f"  (1,1) : {game.get_cell(1,1)}")
print(f"  (0,2) : {game.get_cell(0,2)}")
print()


print("----- TEST 3 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(6,7, 4, ["Yellow", "Red"])
print()

print(f"  (5,0) : {game.get_cell(5,0)}")
print(f"  (3,6) : {game.get_cell(3,6)}")
print(f"  (2,4) : {game.get_cell(2,4)}")
print(f"  (1,5) : {game.get_cell(1,5)}")
print(f"  (0,3) : {game.get_cell(0,3)}")
print(f"  (0,6) : {game.get_cell(0,6)}")
print()


print("----- TEST 4 -----")

print("Building the new object...")
game = connect_n_state.Connect_N_State(10,10, 5, ["Red", "Yellow"])
print()

print(f"  (1,6) : {game.get_cell(1,6)}")
print(f"  (7,2) : {game.get_cell(7,2)}")
print(f"  (8,2) : {game.get_cell(8,2)}")
print(f"  (9,4) : {game.get_cell(9,4)}")
print(f"  (5,1) : {game.get_cell(5,1)}")
print(f"  (4,8) : {game.get_cell(4,8)}")
print()


print("TESTCASE COMPLETED")


