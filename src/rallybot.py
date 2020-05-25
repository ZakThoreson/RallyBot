#libraries
import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
import boto3
#Components
import help, builds, registration



# Get the database
db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#Load the token from environmental variables, which must be set on the machine
#before running the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

#Saves sessions for commands that require multiple responses
sessions = db.Table('sessions')

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


    #Command Switch
    ###########################################################
    #Handle Public commands
    ###########################################################

    #Usage message
    if tokens[0] == '!help':
        await message.channel.send(embed=help.usage())

    #List/Search builds
    elif tokens[0] == '!builds':
        embed = builds.builds(tokens[1:])
        await message.channel.send(embed=embed)

    ###########################################################
    #Handle Private commands
    ###########################################################

    #User is DMing the bot
    elif(isinstance(message.channel, discord.DMChannel)):

        if(tokens[0] == '!register'):
            sessions.update_item(
                Key = {
                    'id' : message.author.id
                },
                UpdateExpression = 'SET command = :val1',
                ExpressionAttributeValues = {
                    ':val1' : 'register'
                } 
            )

        response = sessions.get_item(
            Key = {
                'id' : message.author.id
            }
        )
        
        if('Item' in response):
            if(response['Item']['command'] == 'register'):
                embed = registration.registrationSwitch(message)
                await message.channel.send(embed = embed)
        else:
            #Unknow command, why are you whispering the bot?
            embed = discord.Embed(title='Unexpect Input', \
                description="\'%s\' was unexpected." % (message.content), color=0xFF0000)
            #echo command
            await message.channel.send(embed = embed)
            #send usage
            await message.channel.send(embed = help.usage())

    ###########################################################
    #Handle Error Messages
    ###########################################################

    #Functionally required with an added bonus of anit-spam, command must be DMed
    elif tokens[0] == '!register':
        embed = discord.Embed(title='Private Command', description="To prevent spam, the \'%s\' command can only be used through a direct message to the bot." % (tokens[0]), color=0xFF0000)
        await message.channel.send(embed = embed)

            


client.run(TOKEN)
