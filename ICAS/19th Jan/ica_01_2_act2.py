import random


def random_rolls(s):
    random.seed(s)
    number = random.randint(1,20)
    total = 0
    while(1):
        if number == 1:
            print("Rolled a 1, the loop \
                will now terminate.")
            break
        elif number == 20:
            print("Rolled a 20, I will add double \
                the value to the running sum.")
            total +=40
            print("  Sum so far: "+str(total))   
        else: 
            print("Rolled a "+str(number)+\
                ",  I will add the value to the running sum.")
            total+=number
            print("  Sum so far: "+str(total))
        number = random.randint(1,20)
    return(total)
  
        

            
