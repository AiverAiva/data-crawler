import sys
import requests
import os
import json
import time

guildList = requests.get('https://api.wynncraft.com/public_api.php?action=guildList').json()['guilds']

path = os.path.join('data', 'wynncraft', 'guildprefix.json')
with open(path, 'r') as f:
    prefixData = json.load(f)

# existedGuild = list(map(lambda x: prefixData[x], prefixData))
existedGuild = {k: v for v, k in prefixData.items()}
duplicatedGuild = ['Mlg', 'Mortal Assassins', 'Masters of Wynn', 'The Luc Squad', 'SwagSquad', 'Britania', 'Legalthea', 'Wynnter of anar', 'Wynn Warriors', 'Ketsueki Akuma', 'Elite', 'DarkVictory', 'LegendsOfLeague', 'RPG', 'WynnGalaxys', 'Bounty of Wynn', 'WorldOfWynncraf', 'Guards of Wood', 'Thunderbolt', 'Mages of Wynn', 'Frost Clan', 'Wynncrafters', 'Gods of Death', 'Sword Art Onlin', 'Team CM', 'Swag Squad', 'Crescent', 'Knights of Blood', 'Shadows of Wynn', 'The Super Yetie', 'the assassins', 'TotallyLegal', 'Megitsune', 'RunesForWynn', 'DiamondArmy', 'GrimmMechas', 'DIXX', 'White Lotus', 'LucHacks', 'Social Assistance', 'gods of dungeon', 'dingfriesrdone', 'WynnGalaxy', 'Bakers Of Wynn', 'HealthyxApple', 'Shop', 'Knight Of Blood', 'WarriorsofWynn', 'Templar Lusitania', 'SAD Industries', 'Mythical', 'RMS', 'Ramu of Wynn', 'ImperialGold', 'TheSmartWynns', 'Stars Of Night', 'French Cube', 'WynnWalrus', 'Grimm', 'meme', 'Kartoshechka', 'team t tree', 'Moments', 'Theoricks Staff', 'The Memers', 'Darkest Descent']

for i in guildList:
    if (i in existedGuild): 
        pass
        # print(f"{i} passed")
    elif (i in duplicatedGuild):
        pass
    else:
        print(f"Processing {i}")
        guildData = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={i}').json()
        prefixData[guildData['prefix']] = i
        with open(path, 'w') as f:
            json.dump(prefixData, f)
        # time.sleep(0.4)

# for i in guildList:
#     if (i not in existedGuild): 
#         try:
#             guildData = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={i}').json()
#             prefixData[guildData['prefix']] = i
#             with open(path, 'w') as f:
#                 json.dump(prefixData, f)
#             time.sleep(0.4)
#         except:
#             print(f"Error happens on processing {i}")
