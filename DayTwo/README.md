# Day Two Guide
Day Two shows the students how to create their own Discord bot. It will require them to create a server, an app for the server, and a bot account for the app. Then, they will be able to run a Python script to activate their bot.

## Review Kahoot Quiz
There is a Kahoot reviewing the concepts covered on Day One. The Kahoot is especially geared toward the background knowledge needed for Day Two, although it only covers topics that have already been taught.

[Link](https://play.kahoot.it/#/k/fc7e9263-eab1-48db-94ec-986ebd0f2641)


## Initial Setup
### Discord Setup
Walk through the steps from `DiscordSetup.md` to help the students setup their bot accounts.

### Running and explaining the starting bot code
Students should open VS Code, where they should have a copy of the starting bot Python script. Then:
1. Replace the `TOKEN` variable value with the token copied from their bot app
1. Run the script from the **Debug** pane by clicking the start button
1. Back on the Discord Server, verify that the bot appears online
1. Send a message of "hello" and verify that the bot responds with "hi!"

Once all the students have their bots online and responsive, explain the basics of the code. There are some new concepts used in the code, but hopefully they will not be too confusing. These concepts are _function parameters_ and _return statements_.
- The students should not have to worry about anything under the large "Bot code" comment. Instructors can explain it briefly, but does not require in-depth explanation.
- The `respond_to_message` function takes in a `message` and _returns_ a response.
- Right now, it simply checks if the message is "hello" and returns "hi!" in that case. Otherwise, it returns the empty string ("").


## Follow-Along Activity
The goal of the follow-along activity is to augment the starting bot with the ability to multiply a number by 2. The new code uses the string `replace` method and `str.startswith`, which are new concepts. However, they should not be too hard to understand.

> _Note: It may be helpful to print out the variable values throughout the activity_ 

The instructor should make changes to the code to build it up to the follow bot, completing the following steps:
1. In the `respond_to_message` function, create a new `if` block checking if the message starts with "!multiply"  
    _Note: Start by simply returning an example message to see if it's working_
1. Define a `multiply` function that returns an example number, and call it within `respond_to_message`
1. In the `multiply` function, using the `str.replace` function to extract the number from the message (store it in another variable)
1. Convert the string number into an integer using the `int` function (store it in another variable)
1. Multiply the number by 2 (store it in another variable)
1. Convert the number back into a string (store it in another variable)
1. Return the multiplied string number
1. Test that the bot properly multiplies numbers!


## Individual Exercises
These exercises allow the students to add some new features to the existing bot. They should be able to work from the follow along code, and build it up to the completed file. During this time, the instructors should walk the room and assist the students.


## Challenges
There are options for Challenges in the `Challenges.txt` file. Students can select which challenges they would like to attempt.


## Schedule
| Activity | Time |
|-|-|
| Review Kahoot Quiz | 5:30-5:45 |
| Discord Setup | 5:45-6:30 |
| Break | 6:30-6:45 |
| Follow-Along Activity | 6:45-7:30 |
| Individual/Challenges | 7:30-8:00 |


## References
- [Dev Dungeon Tutorial](https://www.devdungeon.com/content/make-discord-bot-python)
- [API Docs for discord.py](http://discordpy.readthedocs.io/en/latest/api.html)