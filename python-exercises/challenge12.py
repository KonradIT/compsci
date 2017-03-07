########################################
#   Python Game based on POINTLESS BBC #
########################################
import time
import json
import random
import os.path
TEAMS=[]
SAVED_GAME_JSON="saved_game.json"
BATCH_STACK=["Questions about the US", "Questions about Spanish companies", "Questions about math"]
QUESTION_STACK=[""]
if not os.path.isfile(SAVED_GAME_JSON):
    print("Game config not found. Creating new game.")
    with open(SAVED_GAME_JSON, "at") as fe:
        start="\"teams\":{\n\t"
        #print(start)
        fe.write(start)
        comma=","
        teams=int(input("How many teams will be playing: "))
        for i in range(teams):
            if int(teams) - i == 1:
                comma=""
            print("Team " + str(i+1))
            TEAMS.insert(i, input("Enter teamname: "))
            tname="\n\t\""+TEAMS[i]+"\"" + comma
            #print(tname)
            fe.write(tname)
        fe.write("\n},")
        print(TEAMS)
        fe.close()
with open(SAVED_GAME_JSON, "at") as f:
    print("Welcome to Pointless")
    print("Where obvious answers mean nothing\nAnd obscure answers mean everything\nThe less points, the more you win.\nGood luck!")
    print("We will play with the teams from last time.")
    for i in range(len(TEAMS)):
        print("Welcome, team " + str(i+1))
        print("\nDecide: ")
        count=0
        for i in BATCH_STACK:
        	print(" - "+str(count+1) + " - " + str(BATCH_STACK[count]))
        	count += 1
        choice=int(input("Batch: "))
        #print("Question: " + QUESTION_STACK[random.randint(0,10)])
