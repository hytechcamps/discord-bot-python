import discord
import requests
import random

TOKEN = "dfkjngldkjgblshi.dhdfg54fg8+4dgh"
be_fancy = True
known_words = { 'hyland':'Were i was made', 'robot':'An unintelligent machine, definitely not me', 'discord':'A messaging app i live on' }
funcDict = {}

def dictionary(message):
    word = message.split(' ')[1].lower()
    if word in known_words:
        return known_words[word]
    else:
        return "I don't know that word"

def wiki_dictionary(message):
    try:
        words = message.replace("!wiki ", "")
        q = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&search=" + words + "&limit=10")
        q = q.json()
        num = random.randint(2, len(q)-1)
        return q[num][1]
    except:
        return "I couldn't find that word"

def ball8(message):
    message = message.replace("!8ball", "")
    r = requests.get("https://8ball.delegator.com/magic/JSON/" + message)
    r = r.json()
    return r["magic"]["answer"]

def repeat(message):
    words = message.split(' ')
    if len(words) == 2:
        return (words[1]+' ') * 2
    if len(words) == 3:
        return (words[2]+' ') * int(words[1])
    else:
        return "I don't understand"

def multiply(message):
    num_part_str = message.replace("!multiply ", "")
    try:
        if(' ' in num_part_str):
            num1, num2 = num_part_str.split(' ')
            multiplied_num = int(num1) * int(num2)
            str_answer = str(multiplied_num)
            return str_answer
        else:
            return str(int(num_part_str) * 2)
    except:
        return "That wasn't a number"

# computes the requested dice roll in format xDy
def roll_command(message):
    words = message.split(' ')
    num = roll_dice(words[1])
    return str(num)

# Performs a dice roll, expects input string to be in the form
# xDy or xdy, where x is the number of dice and y is the size
def roll_dice(string):
    total = 0
    if len(string) < 3:
        return 0
    string = string.lower()
    if "d" in string:
        d = string.find("d")
    else:
        return 0
    diceval = int(string[d+1:])
    dicecount = int(string[:d])
    for _ in range(0, dicecount):
        total += random.randint(1, diceval)
    return total

# sends a cat fat to chat
def catfact(message):
    q = requests.get("https://catfact.ninja/fact")
    return q.json()["fact"]

# sends the sprite and pokedex entry for the requested pokemon
def pokemon(message):
    try:
        base = "https://pokeapi.co/api/v2/pokemon/"
        message = message.split(" ")
        base = base + message[1].lower()
        q = requests.get(base)
        q = q.json()
        q = q["sprites"]["front_default"]
        return q
    except:
        return "That wasn't a pokemon"

def hello(message):
    return "hi!"

def help(message):
    ret = ""
    for key in funcDict.keys():
        ret += "\n" + key
    return ret

# Python allows you to store functions into variables for later use
funcDict = {
        "!multiply":multiply,
        "!def":dictionary,
        "!wiki":wiki_dictionary,
        "!8ball":ball8,
        "!repeat":repeat,
        "hello":hello,
        "!roll":roll_command,
        "!catfact":catfact,
        "!pokemon":pokemon,
        "!help":help
    }

# Uses the dictionary of functions above to respond to a message
def fancy_respond_to_message(message):
    word = message.split(" ")[0]
    if word in funcDict:
        # gets the corresponding function to what is in message
        # and passes message into that function
        return funcDict[word](message)

    return ""

def respond_to_message(message):
    if be_fancy:
        return fancy_respond_to_message(message)

    if message == "hello":
        return "hi!"

    if str.startswith(message, "!multiply"):
        return multiply(message)

    if str.startswith(message, "!def"):
   	    return dictionary(message)

    if str.startswith(message, "!wiki"):
        return wiki_dictionary(message)

    if str.startswith(message, "!8ball"):
        return ball8(message)

    if str.startswith(message, "!repeat"):
        return repeat(message)

    if str.startswith(message, "!roll"):
        return roll_command(message)

    if str.startswith(message, "!catfact"):
        return catfact(message)

    if str.startswith(message, "!pokemon"):
        return pokemon(message)

    if str.startswith(message, "!help"):
        return help(message)

    return ""



##########################################
# Bot code
##########################################

client = discord.Client()

@client.event
async def on_message(message):
    # if the message is coming from the bot itself, do not respond
    if message.author == client.user:
        return

    # get the response for the message
    response = respond_to_message(message.content)

    # send the response if it's not blank
    if response != "":
        await client.send_message(message.channel, response)

@client.event
async def on_ready():
    print("Logged in")

client.run(TOKEN)