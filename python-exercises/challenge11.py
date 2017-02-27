###Battle soldiers game:
import random, time, os
class Game():
    def __init__(self):
        self.PLAYERS_MONEY=[10, 10]
        self.CURRENT_PLAYER=0
    def add(self, num):
        self.PLAYERS_MONEY[self.CURRENT_PLAYER] =+ num
        print("    Nice shot!\n    You got "+str(num)+" USD added to your account!")

        #os.system('cls')
    def battle(self):

        print("    BATTLE!")
        print("    Attack your opponent")
        self.add(50) if random.randint(0,21) % 2 == 0 else print("    not shot")
        self.print_screen()
    def build(self):
        print("    BUILD!")

        print("What would you like to buy?")
        print("A: House\tB: Shed")
        option = input("Enter: ")
        if option == "A":
            cost = 30
            if(self.PLAYERS_MONEY[self.CURRENT_PLAYER] - cost < - 0):
                print("Unable to buy")
            else:
                print("Enjoy your new house")
                self.PLAYERS_MONEY[self.CURRENT_PLAYER] =- cost
                print("You have ", self.PLAYERS_MONEY[self.CURRENT_PLAYER], " left in budget")
        else:
            cost = 40
            if(self.PLAYERS_MONEY[self.CURRENT_PLAYER] - cost < - 0):
                print("Unable to buy")
            else:
                print("Enjoy your new shed")
                self.PLAYERS_MONEY[self.CURRENT_PLAYER] -= cost
                print("You have ", self.PLAYERS_MONEY[self.CURRENT_PLAYER], " left in budget")

    def print_screen(self):
        if self.CURRENT_PLAYER==0:
            self.CURRENT_PLAYER=1
        else:
            self.CURRENT_PLAYER=0
        print("Welcome to the battle field, player " + str(self.CURRENT_PLAYER) +"\n")
        print("Let's see your options:\n    - [0] Attack the Enemy.\n" + str("    - [1] Build your Military Base" if self.PLAYERS_MONEY[self.CURRENT_PLAYER] > 20 else "    You need at least 20 USD to build an army."))
        print("    Your money: " + str(self.PLAYERS_MONEY[self.CURRENT_PLAYER]) + " USD")
        CHOICE=int(input("    Enter your choice: "))
        self.battle() if CHOICE == 0 else self.build()
        #os.system('cls')

Game().print_screen()
