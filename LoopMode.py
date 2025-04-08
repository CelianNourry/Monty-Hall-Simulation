import random

def setup():
    global howmany, alldoors, carposition
    Goat, Car = False, True
    alldoors = []
    #On demande le nombre de portes, puis on les remplis de "Goat"
    howmany = doorsamount
    alldoors = [Goat] * howmany

    #La position de la voiture est prise au hasard.
    carposition = random.randint(0,howmany-1)

    #On met la voiture dans la liste.
    alldoors[carposition] = Car

    #On demande la porte choisie au joueur
    global playerdoorchoice
    playerdoorchoice = random.randint(0,howmany-1)

    montychoice()

def montychoice():
    #L'hôte choisit une porte au hasard
    global hostdoorchoice
    hostdoorchoice = random.randint(0,howmany-1)

    #Si l'hôte choisit la porte de la voiture ou celle du joueur, la fonction recommence
    if hostdoorchoice == carposition or hostdoorchoice == playerdoorchoice:
        montychoice()

    else: #Sinon, on passe à la fonction switch
        switchfunction()

def switchfunction():
    global noswitchvictoryrate, switchvictoryrate, noswitchdefeatrate, switchdefeatrate

    if switch == False:
        switchquestion = "N"
    else:
        switchquestion = "O"

    #Si on ne change pas de porte
    if switchquestion == "N" or switchquestion == "n":
        if playerdoorchoice == carposition:
            noswitchvictoryrate += 1
        else:
            noswitchdefeatrate += 1

    #Si on change de porte
    else:
        doorswitch = random.randint(0,howmany-1) #Un deuxième porte est choisie au hasard
        if doorswitch == hostdoorchoice or doorswitch == playerdoorchoice: #Si c'est celle de l'hôte/ celle précédemment prise, on recommence
            switchfunction()
        
        else: #Sinon, on voit si la deuxième porte choisie et celle de la voiture
            if doorswitch == carposition:
                switchvictoryrate += 1
            else:
                switchdefeatrate += 1

def montychoiceloop(doors,loops):
    global doorsamount, switch, noswitchvictoryrate, switchvictoryrate, noswitchdefeatrate, switchdefeatrate
    doorsamount = doors
    noswitchvictoryrate, switchvictoryrate, noswitchdefeatrate, switchdefeatrate = 0, 0, 0, 0

    #On créer une constante pour qu'elle soit réutilisée quand on changera de mode.
    loopvalue = loops
    switch = False

    while loops != 0: #Premier mode, on ne change pas de porte
        loops -= 1
        setup()
    loops = loopvalue

    while loops != 0:  #Deuxième mode, on change de porte
        switch = True
        loops -= 1
        setup()


    print("Jamais changer de portes : ")
    print("Victoires : " + str(noswitchvictoryrate) + ". Défaites : " + str(noswitchdefeatrate))
    winrate1 = noswitchvictoryrate * 100 / loopvalue
    print("Le taux de victoire en ne changeant jamais de porte est de " + str(winrate1) + "%.")

    print("")
    print("Toujours changer de portes : ")
    print("Victoires : " + str(switchvictoryrate) + ". Défaites : " + str(switchdefeatrate))
    winrate2 = switchvictoryrate * 100 / loopvalue
    print("Le taux de victoire en changeant toujours de porte est de " + str(winrate2) + "%.")

montychoiceloop(3,100)