
import math



def foo(a,b):
    print(f"foo() was called:  a={a}  b={b}")
    return f"<{a}>" * (b+1)


def bar(b):
    print(f"bar() was called:  b={b}  b squared: {b*b}   b sqrt: {math.sqrt(b)}")
    print("    I will return nothing, so the retval should be 'None'")


def baz(a2,b2):
    print( "baz() was called:")
    print(f"    a2 = {a2}")
    print(f"    b2 = {b2}")
    print(f"    b2 = {b2}    (again)")
    print(f"    a2 = {a2}    (again)")
    combined = f"{a2}|{b2}"
    print(f"    combined: {combined}")
    print( "    baz() is done.")
    return len(combined)

