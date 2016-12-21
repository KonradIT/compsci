#Battle game:
#Created by Konrad Iturbe
import random
player1 = 100 #defines the Health count
player2 = 100 #defines the Health count
randomNumber = ""
playerPlayed=0
lastUsed=0
lastUsedTwo=0
mwCount=0
bwCount=0
mwCountTwo=0
bwCountTwo=0
print("PYTHON SHOOTER GAME")
print("Small weapon = limitless")
print("Medium Weapon = 1 available, does +5 damage")
print("Big Weapon = 1 available, does +10 damage")
print("Game started!")

while playerPlayed != 2:
    #Player 1 plays:
    if(player1 > 0):
        weaponchoice=input("Player 1:\nUse \"b\" for Big Weapon,\"m\" for Medium Weapon,\"s\" for Small Weapon\n")
        if(weaponchoice=="s"):
            points=int(random.randint(0, 10))
            if(points==0):
              print("Missed!")
            else:
              player2=player2-points
              lastUsed=1
        if(weaponchoice=="m"):
            if(mwCount<1):
                player2=player2-int(random.randint(1, 10) + 5)
                lastUsed=5
                mwCount=mwCount+1
                if(player1 < 1):
                    print("Player 1: You have 0 lives, you lost.\n")
                    print("Player 2: Won!\n")
                    exit()
            else:
                print("You have used all your Medium Sized Weapons.\n")
        if(weaponchoice=="b"):
            if(bwCount<1):
                player2=player2-int(random.randint(1, 10) + 10)
                lastUsed=10
                bwCount=bwCount+1
                if(player1 < 1):
                    print("Player 1: You have 0 lives, you lost.\n")
                    print("Player 2: Won!\n")
                    exit()
            else:
                print("You have used all your Big Sized Weapons.\n")


        print("Player 2: " + str(player2) + " points left!\n")
    else:
        print("Player 2: You have 0 lives, you lost.\n")
        print("Player 1: Won!\n")
        exit()
    if(player2 > 0):
        weaponchoice=input("Player 2:\nUse \"bigweapon\",\"mediumweapon\",\"smallweapon\"\n")
        if(weaponchoice=="s"):
            points=int(random.randint(0, 10))
            if(points==0):
              print("Missed!")
            else:
              player1=player1-points
              lastUsedTwo=1
        if(weaponchoice=="m"):
            if(mwCountTwo<1):
                player1=player1-int(random.randint(1, 10) + 5)
                lastUsedTwo=5
                mwCountTwo=mwCountTwo+1
                if(player2 < 1):
                    print("Player 2: You have 0 lives, you lost.\n")
                    print("Player 1: Won!\n")
                    exit()
            else:
                print("You have used all your Medium Sized Weapons.\n")
        if(weaponchoice=="b"):
            if(bwCountTwo<1):
                player1=player1-int(random.randint(1, 10) + 10)
                lastUsedTwo=10
                bwCountTwo=bwCountTwo+1
                if(player2 < 1):
                    print("Player 2: You have 0 lives, you lost.\n")
                    print("Player 1: Won!\n")
                    exit()
            else:
                print("You have used all your Big Sized Weapons.\n")


        print("Player 1: " + str(player1) + " points left!\n")
    else:
        print("Player 2: You have 0 lives, you lost.\n")
        print("Player 1: Won!\n")
        exit()
