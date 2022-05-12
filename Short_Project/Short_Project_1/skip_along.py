x = input()
x = x.strip()
l = len(x)
print("Length (after stripping): ",l)
spliced_word = x
final_str = ""
str_len = l
for i in range(l):
    if str_len < i+1:
        if len(spliced_word)%2 == 0:
            break
        else:
            final_str+=spliced_word
            break
    elif (i+1)% 2 == 1:
        final_str += spliced_word[:i+1]
        final_str += ","
        spliced_word = spliced_word[i+1:]
    elif (i+1)% 2 == 2:
        spliced_word = spliced_word[i+1:]
    str_len -= (i+1)


