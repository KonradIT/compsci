#Battle game:
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
while playerPlayed != 2:
    #Player 1 plays:
    if(player1 > 0):
        weaponchoice=input("Player 1:\nUse \"bigweapon\",\"mediumweapon\",\"smallweapon\" or hit Enter to use the last gun used.\n")
        if(weaponchoice=="smallweapon"):
            player2=player2-int(random.randint(1, 10) + 1)
            lastUsed=1
        if(weaponchoice=="mediumweapon"):
            if(mwCount<1):
                player2=player2-int(random.randint(1, 10) + 5)
                lastUsed=5
                mwCount=mwCount+1
                if(player1 > 0):
                    print("Player 1: You have 0 lives, you lost.\n")
                    print("Player 2: Won!\n")
                    exit()
            else:
                print("You have used all your Medium Sized Weapons.\n")
        if(weaponchoice=="bigweapon"):
            if(bwCount<1):
                player2=player2-int(random.randint(1, 10) + 10)
                lastUsed=10
                bwCount=bwCount+1
                if(player1 > 0):
                    print("Player 1: You have 0 lives, you lost.\n")
                    print("Player 2: Won!\n")
                    exit()
            else:
                print("You have used all your Big Sized Weapons.\n")
        if(weaponchoice==""):
            if(lastUsed == 10 or lastUsed == 20):
                if(mwCount > 1):
                    print("No MSW left\n")
                else:
                    player2=player2-int(random.randint(1, 10) + lastUsed)
                if(bwCount > 1):
                    print("No MSW left\n")
                else:
                    player2=player2-int(random.randint(1, 10) + lastUsed)
            player2=player2-int(random.randint(1, 10) + lastUsed)

        print("Player 2: " + str(player2) + " points left!\n")
    else:
        print("Player 1: You have 0 lives, you lost.\n")
        print("Player 2: Won!\n")
        exit()
    if(player2 > 0):
        weaponchoice=input("Player 2:\nUse \"bigweapon\",\"mediumweapon\",\"smallweapon\" or hit Enter to use the last gun used.\n")
        if(weaponchoice=="smallweapon"):
            player1=player1-int(random.randint(1, 10) + 1)
            lastUsedTwo=1
        if(weaponchoice=="mediumweapon"):
            if(mwCountTwo<1):
                player1=player1-int(random.randint(1, 10) + 5)
                lastUsedTwo=5
                mwCountTwo=mwCountTwo+1
                if(player2 > 0):
                    print("Player 2: You have 0 lives, you lost.\n")
                    print("Player 1: Won!\n")
                    exit()
            else:
                print("You have used all your Medium Sized Weapons.\n")
        if(weaponchoice=="bigweapon"):
            if(bwCountTwo<1):
                player1=player1-int(random.randint(1, 10) + 10)
                lastUsedTwo=10
                bwCountTwo=bwCountTwo+1
                if(player2 > 0):
                    print("Player 2: You have 0 lives, you lost.\n")
                    print("Player 1: Won!\n")
                    exit()
            else:
                print("You have used all your Big Sized Weapons.\n")
        if(weaponchoice==""):
            if(lastUsedTwo == 10 or lastUsedTwo == 20):
                if(mwCountTwo > 1):
                    print("No MSW left\n")
                else:
                    player2=player2-int(random.randint(1, 10) + lastUsed)
                if(bwCount > 1):
                    print("No MSW left\n")
                else:
                    player2=player2-int(random.randint(1, 10) + lastUsed)
            player2=player2-int(random.randint(1, 10) + lastUsed)

        print("Player 2: " + str(player2) + " points left!\n")
    else:
        print("Player 1: You have 0 lives, you lost.\n")
        print("Player 2: Won!\n")
        exit()
