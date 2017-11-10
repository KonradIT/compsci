import random
import time

class RamblingBuck:
	def __init__(self):
		self.battlefield =[[" " for x in range(2)] for y in range(5)]	
		self.battlefield[0][0] = "B"
		self.battlefield[0][1] = "B"
		self.positions=[0,0]
		self.lost=False
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
