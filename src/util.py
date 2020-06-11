'''
Utility functions
'''

import json
import boto3

configFile = './res/config.json'
config = json.load(open(configFile))

#Get the database depending on what environment we're in
db = None
if(config['environment'] == 'PROD'):
    db = boto3.resource('dynamodb')
else:
    db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

sessions = db.Table('sessions')

#return database
def getDB():
    return db

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