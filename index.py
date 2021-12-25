import json
import shutil
import time

chests = [{
    "name": "wood",
    "hp": 80,
    "value": 0.01425
},
{
    "name":"iron",
    "hp": 170,
    "value": 0.0325    
},
{
    "name":"gold",
    "hp": 800,
    "value": 0.1625
},
{
    "name":"diamond",
    "hp": 1300,
    "value": 0.325,
},
{
    "name":"cage",
    "hp": 2000,
    "value": 0
}]
gold = 0
hp = 0
for chest in chests:
    
    response = int(input(f'How many ' + chest['name'] + ' the map have? ' ))
    
    gold += response * chest['value']
    hp += response * chest['hp']

print('.')
time.sleep(0.1)
print('..')
time.sleep(0.1)
print('...')
time.sleep(0.1)
print('----------------------------------------------')

print(f'Total gold: {gold}\n')

fileObj= open('data/dmgHr.txt', 'r')
dmgHr = float(fileObj.read())
fileObj.close()
totalTime = round(hp/dmgHr)
print(f'Total time to finish the map: {totalTime} hours')