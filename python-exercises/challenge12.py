########################################
#   Python Game based on POINTLESS BBC #
########################################
import time
import json
import random
import os.path
TEAMS={"teams":[],"scores":[]}
SAVED_GAME_JSON="saved_game.json"
BATCH_STACK=[["Questions about the US", "Questions about Spanish companies", "Questions about math"],["Questions about WikiLeaks", "Questions about Android OS", "Questions about Uganda", "Questions about The UK"], ["Questions about physics", "Questions about words", "Questions about history"]]
QUESTION_STACK=[["US cities beginning with A", "US cities within 2000 miles from San Diego", "Year with less pollution in NY ever."],["Metropolitan area with the least pop."], "Words ending in ino"]
if not os.path.isfile(SAVED_GAME_JSON):
    print("Game config not found. Creating new game.")
    with open(SAVED_GAME_JSON, "wt") as fe:

        teams=int(input("How many teams will be playing: "))
        for i in range(teams):
            if int(teams) - i == 1:
                comma=""
            print("Team " + str(i+1))
            TEAMS["teams"].append(input("Enter teamname: "))

        print(TEAMS)
        json.dump(TEAMS, fe)
        fe.close()
with open(SAVED_GAME_JSON, "r") as f:
    print("Welcome to Pointless")
    print("Where obvious answers mean nothing\nAnd obscure answers mean everything\nThe less points, the more you win.\nGood luck!")
    print("We will play with the teams from last time:")
    jsonTeams=json.load(f)
    print(jsonTeams["teams"])
    TEAMS=jsonTeams
    for i in range(len(TEAMS)):
        print("Welcome, team " + TEAMS["teams"][i])
        print("\nDecide: ")
        count=0
        randomstack=random.randint(0,2)
        for i in BATCH_STACK[randomstack]:
        	print(" - "+str(count+1) + " - " + str(BATCH_STACK[randomstack][count]))
        	count += 1
        choice=int(input("Batch: "))
        count=0
        for i in QUESTION_STACK[choice-1]:
            count+=1
            print(" Question " + str(count) + " - " + i)
            q_choice=input("Enter question: ")
