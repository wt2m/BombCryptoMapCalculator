import json
import shutil
import sys
import os
from os import walk

print('This action will delete all previous bombers inserted, do you want to continue? (Y/n)')
response = input()
if(response.lower() == 'n'):
    print('closing...')
    sys.exit

aux = 'y'
bombers = []
bombers2 = []
while(aux.lower() != 'n'):
    print('========================================')
    print('Do you want to add other bomber to list? (Y/n)')
    aux = str(input())
    if(aux.lower() == 'n'):
        break
    elif(aux.lower() != 'y'):
        print('Invalid statement')
        continue
    
    damage = int(input('Insert bomber damage: '))
    stamina = int(input('Insert bomber stamina: '))
    speed = int(input('Insert bomber speed: '))
    regen = input('Stamina regen? (Y/n): ')
    recover = input(r'20% chance mana recover? (Y/n): ')
    dmgHr = ((damage * (stamina*50))/(1.6666666666 * stamina))/(1.25-(speed/40))
    if(regen.lower() == 'y'):
        dmgHr *= 2
    if(recover.lower() == 'y'):
        dmgHr *= 1.2
    bomber = {
        'damage': damage,
        'stamina': stamina,
        'regen': regen.lower(),
        'recover': recover.lower(),
        'dmgHr': dmgHr
    }
    bombers.append(json.dumps(bomber))
    bombers2.append(bomber)

print('========================================')
result = json.dumps(bombers)
fileObj = open("data/bombers.json", 'w')
fileObj.write(f"{result}")
fileObj.close()  

totalDmg = 0
for bomber in bombers2:
    totalDmg = totalDmg + float(bomber['dmgHr'])
    
fileObj= open('data/dmgHr.txt', 'w')
fileObj.write(f"{totalDmg}")
fileObj.close()

        