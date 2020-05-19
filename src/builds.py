import discord
import json
#Path to the file that contains all build information
buildFile = './res/builds.json'
metaBuilds = json.load(open(buildFile))


def dpsBuilds():

    #Create embed message and title it
    embed=discord.Embed(title="DPS Builds ", description="Current EK meta DPS builds ", color=0xff0000)
    
    #loop over each class in the hashmap and add it to the message
    for profession in metaBuilds:

        value = ""

        #loop over each build for the class and add it if its damage
        for build in metaBuilds[profession]:
            if( metaBuilds[profession][build]["role"] == "damage" ):
                value += ("[%s](%s)\n" % (build, metaBuilds[profession][build]["link"]))
        
        #Add the profession to the message
        if(value != ""):
            embed.add_field(name=profession, value=value, inline=False)
    
    #Return the embed, which now contains build info for dps builds
    return embed

def supportBuilds():

    #Create embed message and title it
    embed=discord.Embed(title="Support Builds", description="Current EK meta support builds", color=0x00ff00)
    
    #loop over each class in the hashmap and add it to the message
    for profession in metaBuilds:

        value = ""

        #loop over each build for the class and add it if its damage
        for build in metaBuilds[profession]:
            if( metaBuilds[profession][build]["role"] == "support" ):
                value += ("[%s](%s)\n" % (build, metaBuilds[profession][build]["link"]))
        
        #Add the profession to the message
        if(value != ""):
            embed.add_field(name=profession, value=value, inline=False)
    
    #Return the embed, which now contains build info for dps builds
    return embed

def searchBuilds(search):
    #Create embed message and title it
    embed=discord.Embed(title="Search Builds", description="Return builds related to: %s" % (search), color=0x00ff00)
    
    #loop over each class in the hashmap and add it to the message
    for profession in metaBuilds:

        value = ""

        #loop over each build for the class and add it if its damage
        for build in metaBuilds[profession]:
            if( search.lower() in profession.lower() or search.lower() in build.lower() ):
                value += ("[%s](%s)\n" % (build, metaBuilds[profession][build]["link"]))
        
        #Add the profession to the message
        if(value != ""):
            embed.add_field(name=profession, value=value, inline=False)
    
    #Return the embed, which now contains build info for dps builds
    return embed

#Switch based on params that handles the builds command
def builds(params):

    #Return all builds
    if(len(params) == 0):
        return searchBuilds('')
    #Return all dps/damage builds
    if(params[0].lower() == 'dps' or params[0].lower() == 'damage'):
        return dpsBuilds()

    #Return all support builds
    elif(params[0].lower() == 'support'):
        return supportBuilds()

    #Search by class/spec
    else:
        return searchBuilds(params[0])