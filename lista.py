import random
high_scores = [1000,950,850,700,675,550,443,414,395,380]
prices = [9.99, 10.25, 19.99, 100.0]
dog_breeds = ["Poodle","Collie","Terrier","Beagle",]
logicalResults = [True,True,False,True]
collection = [1000, 3.14159, "Carrots", False]
fav_games = ["minecraft","World of Warcraft","geometry dash","super metroid","warcraftIII","tf2","stellaris","cortex command",
                     "terraria","g-mod","oxygen not included","astroneer","starbound","space engineers","super mario maker 2",
                     "Super smash brothers ultimate","breath of the wild","castle crashers","lego star wars III","portal 2"]
print(type(fav_games))
print(len(fav_games))
for i in fav_games:
    if i == "World of Warcraft":
        print("Wow found")
        
    else:
        print("not it")

fav_games[0] = "World of warcraft"
if len(fav_games)!=20:
    print("fail")
elif "fortnite" in fav_games or "Fortnite" in fav_games:
    print("fail")
elif fav_games[0] != "World of warcraft":
    print("fail")
else:
    print("pass")
##print(fav_games)
##print(fav_games[0])
##
##
##for i in fav_games:
##    print(i)

##for i in range(0,21):
##    print(fav_games[i])
#BAD
##for i in range(0,len(fav_games)):
##    print(fav_games[i])

num = random.randint(0,len(fav_games)-1)
print(fav_games[num])
fav_games[5] = "updated"
print(fav_games)
worst_games = ["robocraft","roblox","fortnite","pubg","microsoft edge","ff12","ff11","ff10","ff9","neverwinter","battlefront 2 New","destiny 2","overwatch","hearthstone","call of duty","legend of zelda 1","runescape","league of legends","mario kart tour"]
for i in worst_games:
    print(i)
print(len(worst_games))
