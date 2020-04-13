print("I am the Quiz Master. Would you like to take my Math quiz? Enter if you dare...")
print()

num_correct = 0

# Calculate the score for a given number of correct answers
def calc_score(num):
    fraction_score = num / 5
    percent_score = fraction_score * 100
    str_score = str(percent_score) + "%"

    return str_score

q1 = input("1. What is 5+5?\n")
if q1 == "10":
    num_correct += 1
    print("Correct!")
elif q1 == "11":
    print("Close, but still wrong!")
else:
    print("Wrong!")

print()

q2 = input("2. What is 46*2?\n")
if q2 == "94":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

print()

q3 = input("3. What is the mean of 8, 5, 15, and 12?\n")
if q3 == "10":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

print()

q4 = input("4. What is the greatest common factor of 12, 15, and 42?\n")
if q4 == "3":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

q5 = input("5. What is 5?")
if q5 == "5":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

print()

print("Congratulations, you scored " + calc_score(num_correct))
print("Thank you for taking my quiz...")