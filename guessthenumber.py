import random
print ("pick a # 1-100:")
number = int(input())
randomnumber = random.randrange(1,100)
if number == randomnumber:
    print("you did it!")
elif number > 100 or number < 0:
    print("smart one")
else:
    if number > randomnumber: 
        wrong = number - randomnumber
    else:
        wrong = randomnumber - number
    print("you were " + str(wrong) + " off")
