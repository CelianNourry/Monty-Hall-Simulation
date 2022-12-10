import random

Goat, Car = False, True
alldoors = []
#On demande le nombre de portes, puis on les remplis de "Goat"
howmany = int(input("Avec combien de portes voulez-vous jouer ?"))
alldoors = [Goat] * howmany

#La position de la voiture est prise au hasard.
carposition = random.randint(0,howmany-1)

alldoors[carposition] = Car
print("Random car position :" + str(carposition) +". Position de la voiture dans la liste : " + str(alldoors.index(True)))

#Listes avec les noms réels
l =[]
for i in alldoors:
    if i == False:
        l.append("Goat")
    else:
        l.append("Car")
print("Liste complète : " + str(alldoors))

#On demande la porte choisie au joueur
playerdoorchoice = int(input(str(howmany) + " portes se dressent devant vous, laquelle allez vous choisir d'ouvrir ?"))
print("Porte choisie par le joueur : "+ str(playerdoorchoice))
print("L'hôte décide d'ouvrir une porte...")

def montychoice():
    global hostchoice
    hostchoice = random.randint(0,howmany-1)

    #Si l'hôte choisit la porte de la voiture ou celle du joueur, il en rechoisit une autre au hasard
    if hostchoice == alldoors.index(True) or hostchoice == playerdoorchoice:
        print("Choix de l'hôte : "+ str(hostchoice))
        print("Choix de l'hôte : "+ str(hostchoice) + "Choix du joueur : "+ str(playerdoorchoice))
        montychoice()

    else:
        print("L'hôte a choisit d'ouvrir la porte numéro " + str(hostchoice)+". Il y avait une "+ str(alldoors[hostchoice]) + " derrière celle-ci.")
        print("Choix de l'hôte : "+ str(hostchoice))
        switchmonty()

def switchmonty():
    switchquestion = str(input("Voulez-vous changer de porte ? O si Oui, N si Non."))

    #Si la réponse est invalide
    if switchquestion != "N" and switchquestion != "n" and switchquestion != "O" and switchquestion != "o":
        print("Veillez choisir une réponse valide.")
        switchmonty()
    #Si on ne change pas de porte
    elif switchquestion == "N" or switchquestion == "n":
        print("Pas changé")
        if playerdoorchoice == alldoors.index(True):
            print("Gagné !")
        else:
            print("Perdu...")

    #Si on change de porte
    elif switchquestion == "O" or switchquestion == "o":
        print("Changé") 
        doorswitch = int(input("Vous aviez choisit la porte " + str(playerdoorchoice) + " et l'hôte a choisit d'ouvrir la porte "+ str(hostchoice) + ", revelant une chèvre. Quelle porte choisissez vous d'ouvrir à présent ?"))

        
        if doorswitch == hostchoice:
            print("Vous ne pouvez pas choisir la porte que l'hôte a ouvert.")
            switchmonty()
        if doorswitch == playerdoorchoice:
            print("Vous ne pouvez pas choisir la porte que vous avez voulu ouvrir en premier.")
            switchmonty()
        else:
            if doorswitch == carposition:
                print("Gagné !")
                exit()
            else:
                print("Perdu...")
                exit()

def montychoiceloop():
    loop = True
montychoice()