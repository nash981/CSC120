#! /usr/bin/python3

import random


end_count   = random.randint(2,20)
total_count = end_count+1 + random.randint(0,20)

nums = [ random.randint(-50,100) for _ in range(total_count) ]
nums[end_count] = -1

while nums != []:
    if random.randint(1,3) == 3:
        print(" "*random.randint(0,5))
        continue

    this_len = random.randint(1,5)
    these_nums = nums[ : this_len   ]
    nums       = nums[   this_len : ]

    line  = " "*random.randint(0,5)
    line += str(these_nums[0])
    for num in these_nums[1:]:
        line += " "*random.randint(1,5)
        line += str(num)
    line += " "*random.randint(0,5)

    print(line)

