import random
import time

class RamblingBuck:
	def __init__(self):
		self.battlefield =[[" " for x in range(2)] for y in range(5)]	
		self.battlefield[0][0] = "B"
		self.battlefield[0][1] = "B"
		self.positions=[0,0]
		self.lost=False
		print("  _____                 _     _ _               ____             _    ")
		print(" |  __ \               | |   | (_)             |  _ \           | |   ")
		print(" | |__) |__ _ _ __ ___ | |__ | |_ _ __   __ _  | |_) |_   _  ___| | __")
		print(" |  _  // _` | '_ ` _ \| '_ \| | | '_ \ / _` | |  _ <| | | |/ __| |/ /")
		print(" | | \ \ (_| | | | | | | |_) | | | | | | (_| | | |_) | |_| | (__|   < ")
		print(" |_|  \_\__,_|_| |_| |_|_.__/|_|_|_| |_|\__, | |____/ \__,_|\___|_|\_\")
		print("                                         __/ |                        ")
		print("                                        |___/                         ")
	def printbattlefield(self):
		for i in self.battlefield:
			print(str(i).replace("[","").replace("]","").replace(",",""))
	def bombard(self, channel):
		print(">>> Bombarding {}".format(channel))
		indicator=0
		opponent=0
		if channel == 1:
			indicator=1
			opponent=0
		else:
			indicator=0
			opponent=1
		if self.battlefield[self.positions[opponent]][opponent] == "X":
			self.positions[opponent]=self.positions[opponent]+1
			self.battlefield[self.positions[opponent]][opponent] = B"
		else:
			self.battlefield[self.positions[opponent]][opponent] = "X"
		self.battlefield[self.positions[opponent]][indicator] = " "
		self.battlefield[self.positions[opponent]+1][indicator] = "B"
		self.positions[indicator]=self.positions[indicator]+1
		self.positions[opponent]=self.positions[opponent]+1
bucks = RamblingBuck()
while bucks.lost == False:
	bucks.printbattlefield()
	ch=int(input(">>> Which channel? [1/2]: "))
	bucks.bombard(ch)
