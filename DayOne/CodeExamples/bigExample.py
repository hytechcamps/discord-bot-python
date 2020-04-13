def print_bunny():
    print("()() ")
    print("(o.o)")
    print("(   )")
    print("")

num_bunnies = input("How many bunnies do you want? ")
num_bunnies_int = int(num_bunnies)

if num_bunnies_int > 10:
    print("That's too many bunnies!")
elif num_bunnies_int < 0:
    print("That's not enough bunnies!")
else:
    print("OK!")
    for x in range(num_bunnies_int):
        print_bunny()