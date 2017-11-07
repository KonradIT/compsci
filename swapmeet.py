import random

class SwapMeet:
	def __init__(self):
		self.colors=["R","G","Y","C","P","B"]
		self.arr=[[],[],[],[]]
		self.completed=0
		self.avail=[]
		for i in range(4):
			for i2 in range(6):
			  self.arr[i].append(self.colors[random.randint(0,5)])
		self.printboards()
	def printboards(self):
		for index, i in enumerate(self.arr):
		  print(">Player " + str(index+1) + ": " + str(i).replace("'","").replace(",","").replace("[","").replace("]",""),end="\n\n")
	def available_ppl(self):
	  print("Aval: ", end="- ")
	  self.avail = []
	  for i in range(4):
	    c=self.colors[random.randint(0,4)]
	    self.avail.append(c)
	    print(c,end=" ")
	  print()

	def play(self, player):
	  print("Player " + str(player+1) + " turn now")
	  character1=int(input("Character to replace [from 1 to 6]: "))
	  character2=input("Replace " + self.arr[player][character1-1] + " with " + str(self.avail) + ": ")
	  self.arr[player][character1-1] = character2
	  if self.arr[player][0] == self.arr[player][1] and self.arr[player][1] == self.arr[player][2]:
	    print("You won the first row!")
	  if self.arr[player][3] == self.arr[player][4] and self.arr[player][4] == self.arr[player][5]:
	    print("You won the second row!")
	  if self.arr[player][0] == self.arr[player][1] and self.arr[player][1] == self.arr[player][2] and self.arr[player][2] == self.arr[player][3] and self.arr[player][3] == self.arr[player][4] and self.arr[player][4] == self.arr[player][5]:
	    print("Congratulations!\nYou won the game!\n")
	    exit()
sw = SwapMeet()
while sw.completed != 4:
  for i in range(4):
    sw.available_ppl()
    sw.play(i)
    sw.printboards()
