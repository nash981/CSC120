filename = input()
text = open(filename,'r')
for lines in text:
    length = len(lines)
    print("Line length:",length)
    print(lines)