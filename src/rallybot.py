#libraries
import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
#Components
import help
import builds

#Load the token from environmental variables, which must be set on the machine
#before running the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

#commands setup
#bot.remove_command('help')

#confirm login
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Support Builds
@client.event
async def on_message(message):
    
    #Do not parse our own messages
    if message.author == client.user:
        return

    #Command switch, parse the message and send the parameters
    #parse message into tokens
    tokens = message.content.split(' ')
    if tokens[0] == '!help':
        await message.channel.send(embed=help.usage())

    elif tokens[0] == '!builds':
        embed = builds.builds(tokens[1:])
        await message.channel.send(embed=embed)


client.run(TOKEN)
