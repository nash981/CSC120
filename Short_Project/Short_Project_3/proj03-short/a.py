all = [10, None]
tail = all
# DRAW HERE
for i in range(4):
    tail[1] = [ i*10+20, None ]
    print(tail,tail[1],all)
    tail = tail[1]
    print(tail,all)
# DRAW HERE
print(all)