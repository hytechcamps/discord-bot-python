import discord

TOKEN = "NDQ3MDkyNTUzNzc1NTc5MTQ5.DeRSGA.iqx83L1SSl8NKy2BNahOGCBMUO8"

def multiply(message):
    num_part_str = message.replace("!multiply ", "")
    num_part = int(num_part_str)
    multiplied_num = num_part * 2
    str_answer = str(multiplied_num)

    return str_answer

def repeat(message):
    message_part = message.replace("!repeat ", "")

    return message_part

def respond_to_message(message):
    if message == "hello":
        return "howdy!"

    if message == "goodbye":
        return "bye!"
    
    if str.startswith(message, "help"):
        return "sorry, I can't help you."

    if str.startswith(message, "!multiply"):
        return multiply(message)

    if str.startswith(message, "!repeat"):
        return repeat(message)

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