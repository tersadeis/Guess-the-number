import random
print ("pick a # 1-100:")
x = int(input())
y = random.randrange(1,100)
if x == y:
    print("you did it!")
elif x > 100 or x < 0:
    print("smart one")
else:
    if x > y: 
        rip = x - y
    else:
        rip = y - x
    print("you were " + str(rip) + "off")