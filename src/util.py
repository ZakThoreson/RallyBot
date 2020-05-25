'''
Utility functions
'''

import json
configFile = './res/config.json'
config = json.load(open(configFile))

#return full config file
def getConfig():
    return config

#return value from config file
def getConfigValue(key):
    return config[key]