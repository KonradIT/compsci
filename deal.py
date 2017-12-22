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
		print(self.boxes)
		print("====== WELCOME TO DEAL|!DEAL ======\n>>> Please choose a box.")
		print("| ",end="")
		for i in self.boxes:
			print(i[0],end=" | ")
		self.playerbox=int(input("\n>>> $ "))
		self.startGame()
	def startGame(self):
		print("Prizes available:")
		print(str(self.moneytodisplay).replace("[","").replace("]","").replace(",","$").replace("\'",""),end="$\n")
		print("OK Player, enter a box: ")
dond = DealOrNoDeal()
