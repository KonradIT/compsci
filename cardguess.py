#Card Game from Super Mario

import random

class CardGame:
	def __init__(self):
		self.setup()
		check=True
		self.lost=False
		
		while check:
			if self.cardarray[0][0] == self.cardarray[1][0]:
				for i in self.cardarray:
					random.shuffle(i)
			elif self.cardarray[0][1] == self.cardarray[1][1]:
				for i in self.cardarray:
					random.shuffle(i)
			elif self.cardarray[0][2] == self.cardarray[1][2]:
				for i in self.cardarray:
					random.shuffle(i)
			else:
				check=False
	def setup(self):
		self.tries=0
		self.userarray=[["?","?","?"],["?","?","?"]]
		self.cardarray=[["A","B","C"],["A","B","C"]]
		for i in self.cardarray:
			random.shuffle(i)
	def display_cards(self):
		print("    1    2    3")
		for index,i in enumerate(self.userarray):
			print(index + 1,i)
	def shuffle(self):
		self.tries += 1
		if self.tries == 3:
			self.lost = True
		for i in self.cardarray:
			for j in range(3):
				i.append(random.choice("AABBCC"))
	def enter_data(self):
		
		col1=int(input("Enter column: "))
		row1=int(input("Enter row: "))
		self.userarray[row1-1][col1-1] = self.cardarray[row1-1][col1-1]
		self.display_cards()
		col2=int(input("Enter column: "))
		row2=int(input("Enter row: "))
		self.userarray[row2-1][col2-1] = self.cardarray[row2-1][col2-1]
		self.display_cards()
		if self.userarray[row1-1][col1-1] == self.userarray[row2-1][col2-1]:
			print("Match!")
			self.setup()
			self.display_cards()
		else:
			print("No Match")
			
game = CardGame()
game.display_cards()
while game.lost == False:
	game.enter_data()
