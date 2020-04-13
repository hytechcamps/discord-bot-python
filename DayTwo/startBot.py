import discord

TOKEN = "NDcxNjQ2MDIzMTM2MTgyMjgy.Djn2SA.kmcIKN8vv_TwgIgoW0HeEJfcOlo"

def respond_to_message(message):
    if message == "hello":
        return "hi!"

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