'''
Utility functions
'''

import json
import boto3

db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
sessions = db.Table('sessions')
configFile = './res/config.json'
config = json.load(open(configFile))

#return full config file
def getConfig():
    return config

#return value from config file
def getConfigValue(key):
    return config[key]

#deletes ongoing session
def deleteSession(discordID):
    response = sessions.delete_item(
        Key = {
            'id' : discordID
        }
    )

#Takes the given map of characters and returns a string message
def charactersToString(characterMap):

    characterStr = ''
    for characterKey in characterMap:
        characterStr += ('%s : %s\n' % (characterKey, characterMap[characterKey]))
    return characterStr