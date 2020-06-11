import asyncio
import aiohttp
import util
import json

endpoint = 'https://api.guildwars2.com/v2/'
testKey = util.getConfigValue('testAPIKey')
guildID = util.getConfigValue('guildID')

#Adds status code to JSON return value
async def handleResponse(response):
    res = {}
    res['body'] = json.loads( await response.text())
    res['status'] = response.status
    return res


async def getCharacterNames(apiKey, session):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = await session.get(endpoint + 'characters', headers=headers)
    return (await handleResponse(response))

async def getAccountInfo(apiKey, session):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = await session.get(endpoint + 'account', headers=headers)
    return (await handleResponse(response))

async def getCharacterInfo(apiKey, characterName, session):
    headers = {'Authorization' : 'Bearer ' + apiKey}
    response = await session.get(endpoint + 'characters/' + characterName + '/core', headers=headers)
    return await handleResponse(response)
    
async def getServer(id, session):
    response = await session.get(endpoint + 'worlds?ids=%d' % (id))
    return await handleResponse(response)

