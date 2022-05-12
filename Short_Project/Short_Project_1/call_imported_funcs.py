import short1_thing
a = input()
b = int(input())
outp1 = short1_thing.foo(a,b)
print(outp1)
outp2 = short1_thing.bar(b)
print(outp2)
outp3 = short1_thing.baz(a,b)
print(outp3)
outp4 = short1_thing.foo(outp1,outp3)
print(outp4)

