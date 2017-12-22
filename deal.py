#Deal|!Deal game

import random

class DealOrNoDeal:
	def __init__(self):
		self.moneys=["0.1","0.10","0.50","1","5","10","50","100","250","500","750","1000","3000","5000","10000","15000","20000","35000","50000","75000","100000","250000"]
		self.boxes=[[i+1] for i in range(22)]
		self.moneytodisplay=self.moneys
		self.money = random.sample( self.moneys, len(self.moneys) )
		for index,i in enumerate(self.boxes):
			i.append(self.money[index])
		print("====== WELCOME TO DEAL|!DEAL ======\nInstructions: Attempt to guess the boxes with the least money so the final box has 250k. Bank will make an offer in order to pay less\nEnter a box for you to keep\n")
		print("| ",end="")
		for i in self.boxes:
			print(i[0],end=" | ")
		self.playerbox=int(input("\n>>> $ "))
		self.lost = False
	def startGame(self):
		if len(self.boxes) == 1:
			self.lost = True
		print("| ",end="")
		for i in self.boxes:
			print(i[0],end=" | ")
		print("\nPrizes available:")
		print(str(self.moneytodisplay).replace("[","").replace("]","").replace(",","$").replace("\'",""),end="$\n")
		print("OK Player, enter a box: ")
		box=int(input(">>> # "))
		print("Box " + str(box+1) + " has " + self.boxes[box][1] + "$\n\n")
		self.moneytodisplay.remove(str(self.boxes[box][1]))
		del self.boxes[box]
		
dond = DealOrNoDeal()
while dond.lost == False:
	dond.startGame()
