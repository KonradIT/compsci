#Deal||!Deal game

import random

class DealOrNoDeal:
	def __init__(self):
		self.moneys=["0.1","0.10","0.50","1","5","10","50","100","250","500","750","1000","3000","5000","10000","15000","20000","35000","50000","75000","100000","250000"]
		self.boxes=[[i+1] for i in range(22)]
		self.moneytodisplay=self.moneys
		self.money = random.sample( self.moneys, len(self.moneys) )
		for index,i in enumerate(self.boxes):
			i.append(self.money[index])
		print("====== WELCOME TO DEAL||!DEAL ======\nInstructions: Attempt to guess the boxes with the least money so the final box has 250k. Bank will make an offer in order to pay less\nEnter a box for you to keep\n")
		print("| ",end="")
		for i in self.boxes:
			print(i[0],end=" | ")
		self.playerbox=int(input("\n>>> $ "))
		self.lost = False
		self.noshow_money=[]
		self.noshow_box=[]
		self.testarray=[]
		self.prize=0
	def startGame(self):

		print("| ",end="")
		for i in self.boxes:
			if i not in self.noshow_box:
				print(i[0],end=" | ")
				
		print("\nPrizes available:")
		for y in self.noshow_money:
			for index,j in enumerate(self.moneytodisplay):
				if j == y:
					self.moneytodisplay[index]="."
				else:
					self.prize = j
		print(str(self.moneytodisplay).replace("[","").replace("]","").replace(",","$").replace("\'","").replace(".$ ",""),end="$\n")
		print("OK Player, enter a box: ")
		testarray=[]
		print(len(testarray))
		if "." in self.moneytodisplay:
			testarray=self.moneytodisplay.remove(".")
		box=int(input(">>> # "))-1
		if len(self.moneytodisplay) == 1:
			self.lost=True
		print("Box %s has %s" % (str(box+1), self.boxes[box][1]))
		self.noshow_money.append(str(self.boxes[box][1]))
		self.noshow_box.append(self.boxes[box])
	def announce(self):
		print("Your prize is: %s" % str(self.prize))
		if str(self.prize) is not "250000":
			print("You lost, you did not get 250000 as the last box.")
dond = DealOrNoDeal()
while dond.lost == False:
	dond.startGame()
	if dond.lost == True:
		dond.announce()
		break
