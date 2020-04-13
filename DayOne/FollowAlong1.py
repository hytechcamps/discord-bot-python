print("Zoltar is here to give you the wisdom of the ancients. Answer these questions to hear your fortune......\n")

lifespan = 80

bananas = input("Do you like bananas? (y/n) ")
if bananas == "y":
    lifespan += 20

sign = input("What is your astrological sign? ")
if sign == "Libra":
    lifespan += 5

age_str = input("How old are you? ")
age_num = int(age_str)
lifespan += 25 - age_num

print("You will live to be " + str(lifespan) + " years old!")