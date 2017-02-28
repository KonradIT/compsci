###Battle soldiers game:
import random, time, os, sys
class Game():
    def __init__(self):
        self.PLAYERS_MONEY=[10, 10]
        self.CURRENT_PLAYER=0
    def add(self, num):
        self.PLAYERS_MONEY[self.CURRENT_PLAYER] =+ num
        time.sleep(2)
        print("    >>>Nice shot!\n    >>>You got "+str(num)+" USD added to your account!")
        os.system('powershell -c echo `a')
    def battle(self):

        print("    BATTLE!")
        print("    Attack your opponent:")
        time.sleep(2)
        print("    >>> Aiming weapon\n")
        toolbar_width = 20

        # setup toolbar
        sys.stdout.write("    [%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))

        for i in range(toolbar_width):
            time.sleep(0.1)
            sys.stdout.write("=")
            sys.stdout.flush()

        sys.stdout.write("\n")
        time.sleep(1)
        print("    Fire!")
        time.sleep(0.5)
        self.add(50) if random.randint(0,21) % 2 == 0 else print("    >>>Shot fired: Not shot. Try again next time.")
        time.sleep(5)
        os.system('cls')
        self.print_screen()
    def build(self):
        print("    BUILD!")

        print("    >>>What would you like to buy?\n    >>>Your current amount of money in USD: " + str(self.PLAYERS_MONEY[self.CURRENT_PLAYER]))
        print("    - A: House\n    - B: Shed\n    - C: 15 rounds of Ammo")
        option = input("    >>>Enter: ").upper()
        if option == "A":
            cost = 30
            if(self.PLAYERS_MONEY[self.CURRENT_PLAYER] - cost < - 0):
                print("    >>>Unable to buy")
            else:
                print("    >>>Enjoy your new house")
                self.PLAYERS_MONEY[self.CURRENT_PLAYER] =- cost
                print("    >>>You have ", self.PLAYERS_MONEY[self.CURRENT_PLAYER], " left in budget")
        elif option == "B":
            cost = 40
            if(self.PLAYERS_MONEY[self.CURRENT_PLAYER] - cost < - 0):
                print("    >>>Unable to buy")
            else:
                print("    >>>Enjoy your new shed")
                self.PLAYERS_MONEY[self.CURRENT_PLAYER] -= cost
                print("    >>>You have ", self.PLAYERS_MONEY[self.CURRENT_PLAYER], " left in budget")
        else:
            cost = 30
            if(self.PLAYERS_MONEY[self.CURRENT_PLAYER] - cost < - 0):
                print("    >>>Unable to buy")
            else:
                print("    >>>You have 15 more rounds of Ammo, each round contains 5 bullets.\n    === 75 bullets.")
                self.PLAYERS_MONEY[self.CURRENT_PLAYER] -= cost
                print("    >>>You have ", self.PLAYERS_MONEY[self.CURRENT_PLAYER], " left in budget")
        time.sleep(5)
        os.system('cls')
        self.print_screen()

    def print_screen(self):
        if self.CURRENT_PLAYER==0:
            self.CURRENT_PLAYER=1
        else:
            self.CURRENT_PLAYER=0
        print("    Welcome to the battle field, player " + str(self.CURRENT_PLAYER) +"\n")
        print("    Let's see your options:\n    - [0] Attack the Enemy.\n" + str("    - [1] Build your Military Base" if self.PLAYERS_MONEY[self.CURRENT_PLAYER] > 20 else "    You need at least 20 USD to build an army."))
        print("    Your money: " + str(self.PLAYERS_MONEY[self.CURRENT_PLAYER]) + " USD")
        CHOICE=int(input("    Enter your choice: "))
        self.battle() if CHOICE == 0 else self.build()
        #os.system('cls')
os.system('cls')
Game().print_screen()
