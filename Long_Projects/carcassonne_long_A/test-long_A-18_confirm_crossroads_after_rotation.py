#! /usr/bin/python3

""" Code to test one of the Carcassonne tiles

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE: Testing has_crossroads(), after rotation, for all tiles")
print()

for tile_name,one_tile in [ ("tile01", carcassonne_tile.tile01),
                            ("tile02", carcassonne_tile.tile02),
                            ("tile03", carcassonne_tile.tile03),
                            ("tile04", carcassonne_tile.tile04),
                            ("tile05", carcassonne_tile.tile05),
                            ("tile06", carcassonne_tile.tile06),
                            ("tile07", carcassonne_tile.tile07),
                            ("tile08", carcassonne_tile.tile08),
                            ("tile09", carcassonne_tile.tile09),
                            ("tile10", carcassonne_tile.tile10),
                            ("tile11", carcassonne_tile.tile11),
                            ("tile12", carcassonne_tile.tile12) ]:
    print(f"{tile_name}: Calling has_crossroads() on the original tile, and then on 3 rotations:")
    print(f"    {one_tile.has_crossroads()}")
    one_tile = one_tile.rotate()
    print(f"    {one_tile.has_crossroads()}")
    one_tile = one_tile.rotate()
    print(f"    {one_tile.has_crossroads()}")
    one_tile = one_tile.rotate()
    print(f"    {one_tile.has_crossroads()}")



print()
print("END TESTCASE")

