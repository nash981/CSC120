#! /usr/bin/python3

""" Code to test the trace_city() method of CarcassonneMap

    Author: Russ Lewis
"""

import carcassonne_tile
import carcassonne_map

N = 0
E = 1
S = 2
W = 3



def city_sort(city):
    # we have to sort the set of city elements, since sets do not have a
    # defined order.  But we can't just call sorted() on the trace_city()
    # retval, because it's a (bool,set) tuple
    closed,elements = city
    return (closed, sorted(elements))



print("START TESTCASE")

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()

print("This is the second example city from the Project Overview video...")
game.add(1,0, carcassonne_tile.tile06.rotate()                  , confirm=False)
game.add(1,1, carcassonne_tile.tile06.rotate()                  , confirm=False)
game.add(0,2, carcassonne_tile.tile05                           , confirm=False)
game.add(0,3, carcassonne_tile.tile02.rotate().rotate()         , confirm=False)
game.add(1,3, carcassonne_tile.tile09.rotate().rotate()         , confirm=False)
game.add(1,2, carcassonne_tile.tile14.rotate().rotate().rotate(), confirm=False)
print()

print("Calling trace_city() from various start points:")
print(f"  t_c(0,3,W) returned: {city_sort(game.trace_city(0,3,W))}")
print(f"  t_c(1,2,W) returned: {city_sort(game.trace_city(1,2,W))}")
print(f"  t_c(1,2,N) returned: {city_sort(game.trace_city(1,2,N))}")
print(f"  t_c(0,0,N) returned: {city_sort(game.trace_city(0,0,N))}")
print()

print("END TESTCASE")



# import display_carcassonne_map
# import graphics
# win = graphics.graphics(600,600, "Test")
# display_carcassonne_map.display_map(game, win, 600)
# win.mainloop()

