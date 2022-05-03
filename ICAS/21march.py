arr = [1,1,4,5,3,2,4,5,1,3,5,7,5,4,3,5]
count = len(arr)
i = 0
while i < count:
    j = i + 1
    while j < count:
        if arr[j] == arr[i]:
            arr.pop(j)
            count -= 1
        j += 1
    i += 1
print(arr)
import random
# a = 11
# b = 9
# for i in range(10):
#     question = 'What is",a," x ",b,"? '
#     answer = input(question)
#     if answer == a*b:
#         print("Well done!")
#     else:
#         print("No.")
