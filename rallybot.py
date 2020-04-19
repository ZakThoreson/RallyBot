import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#commands setup
bot = commands.Bot(command_prefix='!', description='A bot assiting EK')
bot.remove_command('help')

#confirm login
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Bot commands

#Support Builds
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!test':
        await message.channel.send('I am working')

    if message.content == '!help':
        embed=discord.Embed(title='Help Menu', description="Current commands supported by the bot", color=0xeee657)
        embed.add_field(name="!builds_support", value="Prints the current EK Support Builds", inline=False)
        embed.add_field(name="!builds_dps", value="Prints the current EK DPS Builds", inline=False)
        await message.channel.send(embed=embed)

    if message.content == '!builds_dps':
        embed=discord.Embed(title="DPS Builds ", description="Current EK meta DPS builds ", color=0xff0000)
        embed.add_field(name="Reaper (Power)", value="http://en.gw2skills.net/editor/?PS0AEd3lVwOYIsEWJeeXntbA-zRRYBRNnvYQBFSThQmVQFJgKDA-e ", inline=False)
        embed.add_field(name="Guardian (Burn)", value="http://en.gw2skills.net/editor/?PWwAYt/lFwQCbdstC3IO+KZrNA-zVRYcRNHPZQDjRiKoeK44iEE9W45TD-w ", inline=False)
        embed.add_field(name="Dragon Hunter", value="http://gw2skills.net/editor/?PWiAENlFwwYdMHWJO0X3tVA-zRJYiRFfh0SEkZJUbCo0hIANL8fGB-e", inline=False)
        embed.add_field(name="Scrapper (Bomb)", value="https://metabattle.com/wiki/Build:Scrapper_-_Big_Bomb_Kit ", inline=False)
        embed.add_field(name="Renegade", value="http://en.gw2skills.net/editor/?PmiAIZldQIMHKi1QSsHCi9RgsASgFzU57G-zRJYnRF/ZkpUIdVgGvEhpHA-e ", inline=False)
        await message.channel.send(embed=embed)

    if message.content == '!builds_support':
        embed=discord.Embed(title="Support Builds", description="Current EK meta support builds", color=0x00ff00)
        embed.add_field(name="Firebrand", value="http://en.gw2skills.net/editor/?PWyAYl7lRwwYdMJmJmyXqvdA-zRJYjRNfZkZKUdF47hIANLtfAA-e", inline=False)
        embed.add_field(name="Scapper (Medic)", value="http://en.gw2skills.net/editor/?Pe0AIp7lNwcYPMP2Je6TntKA-zRJYjRN/ZkpSoaZgknl2PAA-e", inline=False)
        embed.add_field(name="Tempest", value=" http://gw2skills.net/editor/?PG0AgiZlRwSYNMGWJm2WrtdA-zVhYBRQIEdwYYnBfIBJByUF0tQwhXig0bp9DA-w", inline=False)
        await message.channel.send(embed=embed)


client.run(TOKEN)
