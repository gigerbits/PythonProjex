#character inventory
#10/7/2019

import random



#player stats
deff = 0
atk = 1
health = 100
mana = 50
inv = []
equip = []
max_inv = 10
#chest setup
chest_inv = ("gold", "gems", "food", "water", "rusty butter knife","spork",
             "plate with bindings", "cloth hat", "healing kit", "mana potion",
             "arrows", "crocs", "bow", "stick with rock", "cross bow",
             "black shirt", "khaki pants","gucci","Excalafirb","instrumental mayonaise",
             "mocassins", "Doomhammer's Doom Hammer", "magic glasses", "forkknife"
             "fingerless glovels", "centaur in a bucket", "orb of yo momma jokes")
max_chest = 5

items = random.randint(1,max_chest)
chest = []
for i in range(items):
    chest.append(random.choice(chest_inv))
if inv:
    print(inv)
else:
    print("your inventory doesnt feel so good")
    input("open the chest to get your items")
    for items in chest:
        inv.append(items)
print(inv)
for items in inv:
    if items == "healing kit":
        health += 50
        inv.remove("healing kit")

for i in inv:
    if i == "rusty butter knife":
        equip.append("rusty butter knife")
        inv.remove("rusty butter knife")
        atk+=5
for i in inv:
    if i == "spork":
        equip.append("spork")
        inv.remove("spork")
        atk+=1
        deff+=1
for i in inv:
    if i == "plate with bindings":
        equip.append("plate with bindings")
        inv.remove("plate with bindings")
        deff+=3
for i in inv:
    if i == "cloth hat":
        equip.append("cloth hat")
        inv.remove("cloth hat")
        deff+=2
for i in inv:
    if i == "crocs":
        equip.append("crocs")
        inv.remove("crocs")
        deff+=30
for i in inv:
    if i == "bow":
        print("you weeb")
        equip.append("bow")
        inv.remove("bow")
        atk+=1
for i in inv:
    if i == "stick with rock":
        print("range up!")
        equip.append("stick with rock")
        inv.remove("stick with rock")
        atk+=2
for i in inv:
    if i == "cross bow":
        equip.append("cross bow")
        inv.remove("cross bow")
        atk+=2

for i in inv:
    if i == "black shirt":
        print("style up!")
        equip.append("black shirt")
        inv.remove("black shirt")
for i in inv:
    if i == "khaki pants":
        print("legend mode activated")
        equip.append("khaki pants")
        inv.remove("khaki pants")
        health+=200
        deff+=10
for i in inv:
    if i == "gucci":
        print("style up!")
        equip.append("gucci")
        inv.remove("gucci")
for i in inv:
    if i == "Excalafirb":
        equip.append("Excalafirb")
        inv.remove("Excalafirb")
        atk+=10
for i in inv:
    if i =="mocassins":
        print("crocs are better")
        equip.append("mocassins")
        inv.remove("mocassins")
        deff+=1
for i in inv:
    if i =="Doomhammer's Doom Hammer":
        equip.append("Doomhammer's Doom Hammer")
        inv.remove("Doomhammer's Doom Hammer")
        atk+=30
        print("for doomhammer!")
for i in inv:
    if i =="magic glasses":
        print("MathMagical!")
        equip.append("magic glasses")
        inv.remove("magic glasses")
        deff+=3
for i in inv:
    if i =="fingerless glovels":
        print("Gangster's favorite hand warmers")
        equip.append("fingerless glovels")
        inv.remove("fingerless glovels")
        deff+=1
for i in inv:
    if i == "forkknife":
        print("have a good life, not")
        health = 1
        mana = 1
        deff = 0

#repeting chest but bigger
chest_inv = ("gold", "gems", "food", "water", "rusty butter knife","spork",
             "plate with bindings", "cloth hat", "healing kit", "mana potion",
             "arrows", "crocs", "bow", "stick with rock", "cross bow",
             "black shirt", "khaki pants","gucci","Excalafirb","instrumental mayonaise",
             "mocassins", "Doomhammer's Doom Hammer", "magic glasses", "forkknife",
             "fingerless glovels", "centaur in a bucket", "orb of yo momma jokes")
max_chest = 15
items = random.randint(1,max_chest)
chest = []
for i in range(items):
    chest.append(random.choice(chest_inv))      
input("press enter to open the chest")
for i in chest:
    inv.append(i)
if len(inv) > max_inv:
    x = len(inv)- max_inv
    print(inv)
    print("you need to remove "+str(x)+" items")
    while x>0:
        item = input("what item do you want to remove")
        inv.remove(item)
        x-=1
    print(inv)
    input("press enter to equip items")
for items in inv:
    if items == "healing kit":
        health += 50
        inv.remove("healing kit")
for i in inv:
    if i == "rusty butter knife":
        equip.append("rusty butter knife")
        inv.remove("rusty butter knife")
        atk+=5
for i in inv:
    if i == "spork":
        equip.append("spork")
        inv.remove("spork")
        atk+=1
        deff+=1
for i in inv:
    if i == "plate with bindings":
        equip.append("plate with bindings")
        inv.remove("plate with bindings")
        deff+=3
for i in inv:
    if i == "cloth hat":
        equip.append("cloth hat")
        inv.remove("cloth hat")
        deff+=2
for i in inv:
    if i == "crocs":
        equip.append("crocs")
        inv.remove("crocs")
        deff+=30
for i in inv:
    if i == "bow":
        print("you weeb")
        equip.append("bow")
        inv.remove("bow")
        atk+=1
for i in inv:
    if i == "stick with rock":
        print("range up!")
        equip.append("stick with rock")
        inv.remove("stick with rock")
        atk+=2
for i in inv:
    if i == "cross bow":
        equip.append("cross bow")
        inv.remove("cross bow")
        atk+=2

for i in inv:
    if i == "black shirt":
        print("style up!")
        equip.append("black shirt")
        inv.remove("black shirt")
for i in inv:
    if i == "khaki pants":
        print("legend mode activated")
        equip.append("khaki pants")
        inv.remove("khaki pants")
        health+=200
        deff+=10
for i in inv:
    if i == "gucci":
        print("style up!")
        equip.append("gucci")
        inv.remove("gucci")
for i in inv:
    if i == "Excalafirb":
        equip.append("Excalafirb")
        inv.remove("Excalafirb")
        atk+=10
for i in inv:
    if i =="mocassins":
        print("crocs are better")
        equip.append("mocassins")
        inv.remove("mocassins")
        deff+=1
for i in inv:
    if i =="Doomhammer's Doom Hammer":
        equip.append("Doomhammer's Doom Hammer")
        inv.remove("Doomhammer's Doom Hammer")
        atk+=30
        print("for doomhammer!")
for i in inv:
    if i =="magic glasses":
        print("MathMagical!")
        equip.append("magic glasses")
        inv.remove("magic glasses")
        deff+=3
for i in inv:
    if i =="fingerless glovels":
        print("Gangster's favorite hand warmers")
        equip.append("fingerless glovels")
        inv.remove("fingerless glovels")
        deff+=1
for i in inv:
    if i == "forkknife":
        print("have a good life, not")
        health = 1
        mana = 1
        deff = 0
print(atk)
print(deff)
print(health)
print(inv)
print(equip)

    
