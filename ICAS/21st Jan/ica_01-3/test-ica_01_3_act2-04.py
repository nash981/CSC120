#! /usr/bin/python3


from ica_01_3_act2 import *


data = { (0,1,2) : ("abc","def","jkl"),
         (0,1,3) : ("abc","deg","jkl"),
         (2,4,6) : ("abc","def","jklx"),
         (3,5,7) : ("abc","deg") }

print("STARTING DATA:")
for k in data:
    print(f"  {k} : {data[k]}")
print()

print("Calling max_key_by_val()...")
retval = max_key_by_val(data)
print("Call complete.")
print()

print(f"Retval: {retval}")

