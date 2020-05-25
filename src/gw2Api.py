import requests
import util
import json

endpoint = 'https://api.guildwars2.com/v2/'
testKey = util.getConfigValue('testAPIKey')
guildID = util.getConfigValue('guildID')

def getCharacterNames(apiKey):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = requests.get(endpoint + 'characters', headers=headers)
    return json.loads(response.text)

def getAccountInfo(apiKey):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = requests.get(endpoint + 'account', headers=headers)
    return json.loads(response.text)

def getCharacterInfo(apiKey, characterName):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = requests.get(endpoint + 'characters/' + characterName, headers=headers)
    return json.loads(response.text)

