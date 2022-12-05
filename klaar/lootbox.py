## LOOTBOX ##

import random

#open = input("Do you want to open this lootbox? Press E to open. ")

rarity = ["common"]*50 + ["uncommon"]*25 + ["rare"]*13 + ["epic"]*7 + ["legendary"]*4+ ["exotic"]*1

item = random.choice(rarity)
print(item)