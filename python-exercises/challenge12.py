########################################
#   Python Game based on POINTLESS BBC #
########################################
import time
import json
import random
import os.path

SAVED_GAME_JSON="saved_game.json"
if not os.path.isfile(SAVED_GAME_JSON):
    print("Game config not found. Creating new game.")
    open(SAVED_GAME_JSON, "w").close()

with open(SAVED_GAME_JSON) as f:
    #Do stuff
