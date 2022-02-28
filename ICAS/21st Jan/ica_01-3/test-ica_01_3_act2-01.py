#! /usr/bin/python3


from ica_01_3_act2 import *


data = {"foo" : 1234,
        "bar" : 888888,
        "baz" : -1,
        "fred": 256  }

print("STARTING DATA:")
for k in data:
    print(f"  {k} : {data[k]}")
print()

print("Calling max_key_by_val()...")
retval = max_key_by_val(data)
print("Call complete.")
print()

print(f"Retval: {retval}")

