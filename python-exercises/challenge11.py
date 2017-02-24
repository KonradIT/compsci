###Battle soldiers game:
import random, time
PLAYER_1_MONEY=10
PLAYER_2_MONEY=10
CURRENT_PLAYER=1
class Game():
    def __init__(self):
        self._money=0
    def battle(self):
        print("    BATTLE!")
        print("    Attack your opponent")
        print("    " + str("shot" if random.randint(0,5) % 2 == 0 else "not shot"))
    def build(self):
        print("    BUILD!")
    def print_screen(self, player):
        CURRENT_PLAYER_MONEY=0
        x="PLAYER_" + str(player) + "_MONEY"
        CURRENT_PLAYER_MONEY = globals()[x]
        print("Welcome to the battle field, player " + str(CURRENT_PLAYER) +"\nYou're battling againts player " + str(0 if player==1 else 1) + ".")
        print("Let's see your options:\n    - [0] Attack the Enemy.\n" + str("    - [1] Build your Military Base" if CURRENT_PLAYER_MONEY > 20 else "    You need at least 20 USD to build an army."))
        print("    Your money: " + str(CURRENT_PLAYER_MONEY))
        CHOICE=int(input("    Enter your choice: "))
        self.battle() if CHOICE == 0 else self.build()

Game().print_screen(CURRENT_PLAYER)
