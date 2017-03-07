########################################
#   Python Game based on POINTLESS BBC #
########################################
import time
import json
import random
import os.path
TEAMS=[]
SAVED_GAME_JSON="saved_game.json"
if not os.path.isfile(SAVED_GAME_JSON):
    print("Game config not found. Creating new game.")
    with open(SAVED_GAME_JSON, "w")as fe:
        fe.write("\"teams\":{\n\t")
        fe.close()

with open(SAVED_GAME_JSON, "w") as f:
    print("Welcome to Pointless")
    teams=int(input("How many teams will be playing: "))
    for i in range(teams):
              print("Team " + str(i+1))
              TEAMS.insert(i, input("Enter teamname: "))
              f.write("\n\t\""+TEAMS[i]+"\",")

    print(TEAMS)

    #for i in range(len(TEAMS)):
