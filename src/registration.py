"""
Registration/Onboarding interface, user provides GW2 API key and answers
the onboarding questions, which provides the info we need for some of the
bot's functionality.
"""
import discord
import boto3

db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
members = db.Table('members')

#Advances the registration step for the given id by 1
def advanceStep(discordID):

    #get current step value
    response = members.get_item(
        Key = {
            'id' : discordID
        }
    )

    #Advance step by 1
    registrationStep = response['Item']['registrationStep']
    registrationStep += 1

    #Store back in database
    members.update_item(
        Key = {
            'id' : discordID
        },
        UpdateExpression = 'set registrationStep = :in_registrationStep',
        ExpressionAttributeValues = {
            ':in_registrationStep' : registrationStep
        }
    )

#Takes the provided api key, grabs data from it and saves to the db
def apiStep(discordID, apiKey):


#Register the user, occurs in multiple steps
def registrationSwitch(message):

    #Retrieve registrant info from the database
    discordID = message.author.id
    response = members.get_item(
        Key = {
            'id' : discordID
        }
    )

    registrationStep = 0
    info = None

    #Check if registrant is already in database
    if( 'Item' in response):
        #They are in database, grab their info and their registration step
        info = response['Item']
        registrationStep = info['registrationStep']
    else:
        #Not in database, add them as initial step
        members.update_item(
            Key = {
                'id' : discordID
            },
            UpdateExpression = 'set registrationStep = :in_registrationStep',
            ExpressionAttributeValues = {
                ':in_registrationStep' : registrationStep
            }
        )

    #Registration Steps
    description = ''
    if(registrationStep == 0):
        description = 'Welcome to EK Discord! We require an API key to register, which\
             we use to retrieve account/character names, guild status, home world and build info.\
            \nThe API does not provide us with sensitive information such as real name, email address,\
             or passwords.\
            \nPlease direct message this bot your API key with access to account, characters, builds and\
             progression to continue registration....'
        advanceStep(discordID)


    #Retval Creation
    embed=discord.Embed(title = 'Registration Step %d of 3' % (registrationStep),
        description = description, color = 0x00ff00)

    return embed

