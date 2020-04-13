print("I am the Quiz Master. Would you like to take my Math quiz? Enter if you dare...")
print()

num_correct = 0

# Calculate the score for a given number of correct answers
def calc_score(num):
    fraction_score = num / 4
    percent_score = fraction_score * 100
    str_score = str(percent_score) + "%"

    return str_score

# Question 1
q1 = input("1. What is 5+5?\n")
if q1 == "10":
    num_correct += 1
    print("Correct")
else:
    print("Wrong!")

print()

# Question 2
q2 = input("2. What is 46*2?\n")
if q2 == "95":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

print()

# Question 3
q3 = input("3. What is the mean of 8, 5, 15, and 12?")
if q3 == "10":
    num_correct += 1
    print("Correct!")
else:
    print("Wrong!")

print()

# Question 4
q4 = input("4. What is the greatest common factor of 12, 15, and 42?\n")
if q4 == "3":
    num_correct += 2
    print("Correct!")
else:
    print("Wrong!")

print()

print("Congratulations, you scored " + calc_score(num_correct))