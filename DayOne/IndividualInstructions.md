# Day One Individual Exercises

Use `Individual.py` to complete these challenges. Start by running the program and taking the Quiz to see how it works. Then, complete the following exercises.

## Exercise 1 (easy)
Currently, if the user answers Question 1 correctly it will say "Correct" _without_ an exclamation point! Add in the exclamation point so the message matches the others.

## Exercise 2 (easy)
Currently, if the user answers Question 2 with the correct answer (`92`) the Quiz Master will say it is wrong. Change it so that it accepts `92` as the correct answer.

## Exercise 3 (easy)
Currently, when the Quiz Master asks Question 3, the cursor for the answer appears on the same line as the question. Fix this so that the cursor appears on the line below.

>*HINT: Use `\n` at the end of the input string to add the new line*

## Exercise 4 (easy)
Currently, if the user answers Question 4 correctly, the Quiz Master will improperly update the correct answer count by `2`. Fix this so that it updates the correct answer count by `1` instead, matching the other questions.

## Exercise 5 (medium)
At the end of the program, print out another message saying "Thank you for taking my quiz..."

>*HINT: Use the `print` function to accomplish this*

## Exercise 6 (harder)
Currently, if the user answers Question 1 with `11`, the Quiz Master will simply say "Wrong!" and move on. In this case, the Quiz Master should say "Close, but still wrong!" instead. It should still say "Wrong!" for any other answer besides the correct answer and `11`.

>*HINT: Use an `elif` beneath the `if` and above the `else` for Question 1 to handle this*

## Exercise 7 (harder)
Add a whole new question of your choice! This should follow the same format as the other questions.

- Ask the question using the `input` function (store the result in a variable)
- Check the answer using an `if` statement (compare the user's answer to the correct answer with `==`)
- If the user is correct, add to the `num_correct` variable, and print out a message saying "Correct!"
- If the user is incorrect, print out a message saying "Wrong!"
- Finally, update the final score calculation so it divides their score by `5` instead of `4` (change this in the body of the `calc_score` function)