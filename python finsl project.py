import random as r
print("Hello Reader! This is your story generator.")
readername=input("Enter your name here:  ")
print("Hello  " + readername)
names = [' Zara ',' Leah ', ' Sophie ', ' Anina ',' stella ', ' Leona ', ' Emily ']
places = [' Aleria ', ' Italy ', ' America ' , ' Canada ' , ' LA ' , ' Texas ' , ' South Africa ' , ' India ', 'Mumbai ', ' Delhi ']
questes = [' arrive to a grand building and take a photograph ', ' go to meet a celbrity ', ' drive in a large jeep ', ' Eat pizza at the most lavish restaurant you come across ', ' travel on the London Eye in the middle of the night ', ' Buy 20 expensive things in the most extravagant shop they see along the street ',' Go to the most beautiful area they search up in Pakistan ']
roles = [' normal girl ' , ' normal boy ', ' old man ',' teenage girl ',' teenage boy ', 'secondary student ', ' worker at harrods ', ' unversity student ', ' posh girl ']
weather = [' a sunny day ', ' a very humid and hot day ', ' a cold night ', ' a cloudy dat ', ' a rainy day ']
randomname = r.choice(names)
randomplace= r.choice(places)
randomqueste = r.choice(questes)
randomroles= r.choice(roles)
randomweather= r.choice(weather)

story = 'Once upon a time a '+ randomroles +' called ' + randomname + ' lived in a beautiful place called ' + randomplace + ' where it was ' + randomweather + ' and in this place ' + randomname + ' will have to ' + randomqueste
print(story)
