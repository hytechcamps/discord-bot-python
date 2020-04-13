print("Zoltar is here to give you the wisdom of the ancients. Answer these questions to hear your fortune......\n")

lifespan = 80

bananas = input("Do you like bananas? (y/n) ")
if bananas == "y":
    lifespan += 10

sign = input("What is your astrological sign? ")
if sign == "Libra":
    lifespan += 15
elif sign == "Taurus":
    lifespan -= 10
elif sign == "Scorpio":
    lifespan += 5
else:
    lifespan -= 5

def age_calc(age):
    return 20 - age

age_str = input("How old are you? ")
age_num = int(age_str)
lifespan += age_calc(age_num)

height = input("How tall are you in inches? ")
height_num = int(height)

if height_num >= 72:
    lifespan -= 6
else:
    lifespan += 6

print("You will live to be " + str(lifespan) + " years old!")
print("Zoltar thanks you for hearing your fortune....")