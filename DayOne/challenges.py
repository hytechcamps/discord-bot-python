"""
I've organized this file so that challenges can be easily added to and run.
Inside the triple quotes is the name of the person who made it, followed by
the challenge itself.

The 'possible solution' parts are commented out with #, so that they can be easily commented and uncommented
to run specific challenges. (CTRL+K+C to comment selected lines, CTRL+K+U to uncomment.) 

-Peter
"""

"""
 1 - Peter
 Ask the user for two names and print out "Hello, ___ and ___" (printing the names instead of the blanks).
 If you don't know how to start, look back at helloName.py when we asked for one name.

 Possible Solution:
"""
# name1 = input("Name 1?")
# name2 = input("Name 2?")

# print("Hello, " + name1 + " and " + name2)


"""
 2 - Peter
 Ask the user a math problem and tell them if their answer is correct or incorrect.
 When you get the user's input, it will be a string. To change it to a number, use myNumber = int(userInput)
 You don't have to change their answer to a number to see if they are correct. 

Possible Solution:
"""
# userAnswer = input("What is four times six?")

# if userAnswer == "24":
#     print("You are correct!")

# else:
#     print("Sorry, the answer is not " + userAnswer)

"""
3 - Peter
Create a function that prints a message to the console.
'Call' the function so that the message is printed when you 'run' the code.

Possible Solution:
"""
# def printSomething():
#     print("something")

# printSomething()

"""
4 - Peter
This code does not print anything.
Change the if statement so that it will print what it's supposed to.

Now change it to something different that will still print "Yay math :)"
Experiment with different if statements to see if they are true or false.

if(2 + 2 == 5):
    print("Yay math! :)")

Possible Solution:
"""
# if(2 + 3 == 5):
#     print("Yay math! :)")

# if(2 + 2 == 4):
#     print("Yay math! :)")

# if(6):
#     print("Yay math! :)")


""" 1 Jordan- Movie theater

Ask the user for their age
If the user is under 14 print "You are too young to see this movie"

If the users age is between 14 a 16 print "You might be mature enough but Ask your parents first"

If the users age is 17 and up print "You are old enough for this movie have some popcorn on the house"
"""

"""
2 Jordan- Table for 2?

You and your friends when to dinner and now its time to pay 
Everyone agrees to spit the bill evenly 
Ask the user how many people were dining
Ask the user how much was their total bill was
Tell the user how much each person has to pay?

Hint: just incase the class is having a rough time
Divide the total bill by the number of people dining

extra: Include the tax into how much each person pays (20% tax)
"""
"""
3 Jordan- Money in the Bank

Welcome to the Hyland International bank (start each person with 200 dollars)

Ask the user how much money they would like to withdraw. 
If the user ask for more money than they have in there Account
Let them know that they can't take that much money out

After the user takes money out of there account let them know there new balance 
"""
"""
4 Jordan- Guess My Number

Have the user enter a number 
If the user guesses right print "Yah you guessed my number"
If the user guesses wrong print "Better Luck Next Time"

Extra: Have the user keep guessing until they guess the number correct number
"""

"""
5 - Peter - Concert Ticket Prices
Medium difficulty

Ask the user for their age.
Ask the user if they want VIP access.

Regular tickets are $20
Kids under 13 are $10
Seniors (60 and older) are $15

VIP access doubles the ticket price.

Tell the user how much their ticket costs.

Possible Solution:
"""

# age = int(input("Please enter your age: "))
# vip = input("Do you want VIP access? y/n: ")

# price = 20

# if age < 13:
#     price = 10
# elif age >= 60:
#     price = 15

# if vip == "y" or vip == "yes" or vip == "Yes":
#     price *= 2

# print("Your ticket costs " + str(price) + " dollars.")

"""
6 - Peter - Function with parameters.
Medium Difficulty
Create a function that takes two numbers as parameters and adds them together

"Call" your function to solve an addition problem, then print out the answer.
"""
# def add(num1, num2):
#     return num1 + num2

# answer = add(2, 2)

# print(answer)
# #or
# #print(add(2,2))

"""
7 - Peter - Two Functions Number Game
Hard Difficulty

Ask the user to input two numbers. (hint: ask for the first number, then ask for the second number.)
Then ask the user if they want to add or multiply the two numbers.

If they choose "add", add the numbers. If they choose "multiply" multiply the numbers.
Display the final answer to the user.

BONUS: add the numbers in a function called "add", and multiply the numbers in a function called "multiply"
"""
# def add(num1, num2):
#     return num1 + num2

# def multiply(num1, num2):
#     return num1 * num2

# answer = None
# num1 = int(input("What is your first number?"))
# num2 = int(input("What is your second number?"))
# function = input("Would you like to add or multiply? (a/m): ")

# if function == "a":
#     answer = add(num1, num2)
# elif function == "m":
#     answer = multiply(num1, num2)

# print("The answer is: " + str(answer))
