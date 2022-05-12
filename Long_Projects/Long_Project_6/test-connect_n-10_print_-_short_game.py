#! /usr/bin/python3

""" Code to test the Connect_N_State class.  This test focuses on checking to
    see if the print() call works properly.

    Author: Russ Lewis
"""

import connect_n_state



print("Building the new object...")
game = connect_n_state.Connect_N_State(7,6, 4, ["Red", "Yellow"])
print()

MOVES = [0, 5, 1, 6, 0, 3, 2, 5, 6, 2, 0, 6, 2, 1, 3, 6, 1, 0, 1, 6, 2, 6]

for i in range(len(MOVES)):
    move = MOVES[i]

    print(f"---- MOVE {i} : Column {move} ----")
    ok = game.move(move)
    if not ok:
        print("Move was rejected, skipping over it.")
        continue

    game.print()
    print()


print("TESTCASE COMPLETED")


