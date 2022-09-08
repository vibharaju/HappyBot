# happybot.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)
sad_words = set(word.strip() for word in open("negative-words.txt"))

# decorator - basically doing event(on_ready) since event calls an inner function, which is passed as a parameter
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

# Make list of rules for the user and send them when they join as a DM
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to my Discord server!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    for word in sad_words:
        if word in message.content.lower():
            await message.channel.send("Be Positive!")
            dm = await message.author.create_dm()
            await dm.send("Hope everything is alright for you!")
            break

client.run(TOKEN)
