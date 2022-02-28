#! /usr/bin/python3

import shapes



# The tests will use this set to detect unexpected aliasing.  Some aliasing is
# expected and required, of course - but spurious aliasing is always an error!

ids = set()



def test_alpha():
    print("Testing shape_alpha()")

    val = shapes.shape_alpha()

    print(f"shape_alpha() returned: {val}")

    if val[0] != [10,"abc","jkl",40]:
        print("ERROR: Invalid contents")
        return

    if val[1][0] != [1.1,-17]:
        print("ERROR: Invalid contents")
        return

    if val[1][1] != [123,456]:
        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0]))

    if id(val[1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[1]))

    if id(val[1][1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[1][1]))

    print("OK - the shape appears to be correct")



test_alpha()


