import discord

#Print the usage message, which contains info on all available commands
def usage():
    embed=discord.Embed(title='Help Menu', description="Current commands supported by the bot", color=0xeee657)
    embed.add_field(name="!builds_support", value="Prints the current EK Support Builds", inline=False)
    embed.add_field(name="!builds_dps", value="Prints the current EK DPS Builds", inline=False)
    return embed