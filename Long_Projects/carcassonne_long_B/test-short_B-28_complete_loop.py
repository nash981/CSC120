#! /usr/bin/python3

""" Code to test the trace_road_one_direction() method of CarcassonneMap

    Author: Russ Lewis
"""

import carcassonne_tile
import carcassonne_map

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()

game.add(-1, 0, carcassonne_tile.tile11)
game.add(-1,-1, carcassonne_tile.tile04.rotate().rotate().rotate())
game.add( 0,-1, carcassonne_tile.tile06.rotate())
game.add( 1,-1, carcassonne_tile.tile06.rotate())
game.add( 2,-1, carcassonne_tile.tile15.rotate())
game.add( 2, 0, carcassonne_tile.tile15)
game.add( 1, 0, carcassonne_tile.tile06.rotate())

print("Calling trace_road_one_direction() from various start points:")
print(f"  t_r_o_d(0,0,E) returned: {game.trace_road_one_direction(0,0,E)}")
print(f"  t_r_o_d(0,0,W) returned: {game.trace_road_one_direction(0,0,W)}")
print(f"  t_r_o_d(1,0,E) returned: {game.trace_road_one_direction(1,0,E)}")
print(f"  t_r_o_d(2,0,W) returned: {game.trace_road_one_direction(2,0,W)}")

print("END TESTCASE")



# import display_carcassonne_map
# import graphics
# win = graphics.graphics(600,600, "Test")
# display_carcassonne_map.display_map(game, win, 600)
# win.mainloop()

