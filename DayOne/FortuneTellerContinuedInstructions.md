# Fortune Teller Continued

## Exercise 1 (easy)
Currently, liking bananas will add `20` years to the user's lifespan.  
Instead, have it add only `10` years to the user's lifespan.

## Exercise 2 (easy)
Currently, being a Libra will add `5` years to the user's lifespan.  
Instead, have it add `15` years.

## Exercise 3 (medium)
Currently, being a Taurus will add `10` years to the user's lifespan.  
Instead, have it SUBTRACT `10` years.

## Exercise 4 (medium)
At the end of the program, print out another message saying "Thank you for using the fortune teller..."

*HINT: Use the `print` function to accomplish this*

## Exercise 5 (medium)
Currently, when using the `age_calc` function, the fortune teller will add years if the person is under `25` years old.  
Instead, have it only add those years if the person is under `20` years old.

*HINT: Update the value used in the math operation INSIDE the `age_calc` function*

## Exercise 6 (harder)
Currently, the fortune teller only takes into account Libras and Tauruses.  
Add in another astrological sign: Scorpio.  
If the user is a Scorpio, it should add 5 years to their lifespan.

*HINT: Type another `elif` statement under the one for Taurus*

## Exercise 7 (very hard)
>Follow the **Steps** listed below to complete this exercise.

Add in another question asking the user how tall they are in inches. If they are `72` inches or taller, subtract `6` years from their lifespan. If they are shorter than `72` inches, add `2` years to their lifespan.

### Steps
1. Ask the user for their height, and store their response in a variable  
*HINT: Use the `input` function*
2. Convert their height to a number, and store it in another variable  
*HINT: Use the `int` function*
3. Create an `if` structure checking if their height is greater than or equal to `72` (use `>=`)
4. If they are taller than `72` inches, update the lifespan variable by subtracting `6`
5. Otherwise, use an `else` structure and update the lifespan variable by adding `2`