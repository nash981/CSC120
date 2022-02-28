#! /usr/bin/python3


from ica_01_3_act2 import *


data = {1234  : "foo",
        888888: "bar",
        -1    : "baz",
        256   : "fred" }

print("STARTING DATA:")
for k in data:
    print(f"  {k} : {data[k]}")
print()

print("Calling max_key_by_val()...")
retval = max_key_by_val(data)
print("Call complete.")
print()

print(f"Retval: {retval}")

