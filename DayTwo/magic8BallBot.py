import discord
import random

TOKEN = "NDQ3MDkyNTUzNzc1NTc5MTQ5.DeRSGA.iqx83L1SSl8NKy2BNahOGCBMUO8"

def magic_8_ball():
    possible_responses = ["Outlook not so good", "Ask again later", "Signs point to yes", "You may rely on it", "It is decidedly so", "Very doubtful"]
    chosen_response = random.choice(possible_responses)

    return chosen_response

def respond_to_message(message):
    if message == "hello":
        return "hi!"

    if str.startswith(message, "!ask"):
        return magic_8_ball()

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