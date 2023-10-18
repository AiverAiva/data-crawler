import sys
import requests
import os
import json
import time

guildList = requests.get('https://api.wynncraft.com/public_api.php?action=guildList').json()['guilds']

path = os.path.join('data', 'wynncraft', 'guildprefix.json')
with open(path, 'r') as f:
    prefixData = json.load(f)

existedGuild = list(map(lambda x: prefixData[x], prefixData))
print(existedGuild)

for i in guildList:
    if (i in existedGuild): 
        print(f'{i} passed')
    else:
        guildData = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={i}').json()
        prefixData[guildData['prefix']] = i
        with open(path, 'w') as f:
            json.dump(prefixData, f)
    

    

