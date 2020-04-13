print("Zoltar is here to give you the wisdom of the ancients. Answer these questions to hear your fortune......\n")

lifespan = 80

bananas = input("Do you like bananas? (y/n) ")
if bananas == "y":
    lifespan += 20

sign = input("What is your astrological sign? ")
if sign == "Libra":
    lifespan += 5
elif sign == "Taurus":
    lifespan += 10
else:
    lifespan -= 5

def age_calc(age):
    return 25 - age

age_str = input("How old are you? ")
age_num = int(age_str)
lifespan += age_calc(age_num)

print("You will live to be " + str(lifespan) + " years old!")