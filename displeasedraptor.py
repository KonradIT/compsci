import random
class Raptor():
	def __init__(self):
		print(">>> Attacks the swine\n>>> R: Raptor (You)\n>>> T: TNT (AVOID!)\n>>> S: Swine")
		self.Lost = False
		self.Moves = []
	def addMoves(self, move):
		self.Moves.append(move)
	def getMoves(self):
		return self.Moves
	def clearMoves(self):
		self.Moves = []

class Grid():
	def __init__(self):
		print("  _____  _           _                         _   _____             _             ")
		print(" |  __ \(_)         | |                       | | |  __ \           | |            ")
		print(" | |  | |_ ___ _ __ | | ___  __ _ ___  ___  __| | | |__) |__ _ _ __ | |_ ___  _ __ ")
		print(" | |  | | / __| '_ \| |/ _ \/ _` / __|/ _ \/ _` | |  _  // _` | '_ \| __/ _ \| '__|")
		print(" | |__| | \__ \ |_) | |  __/ (_| \__ \  __/ (_| | | | \ \ (_| | |_) | || (_) | |   ")
		print(" |_____/|_|___/ .__/|_|\___|\__,_|___/\___|\__,_| |_|  \_\__,_| .__/ \__\___/|_|   ")
		print("              | |                                             | |                  ")
		print("              |_|                                             |_|                  ")

		self.TheGrid=[["." for x in range(10)] for y in range(6)]
		self.raptorpos=[]
		self.TheGrid[random.randint(0,5)][random.randint(0,9)] = "T"
		self.TheGrid[random.randint(0,5)][random.randint(0,9)] = "S"
		self.raptorpos = [random.randint(0,5),random.randint(0,9)]
		self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] = "R"

	def printgrid(self):
		for i in self.TheGrid:
			print("   " + str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
	def moveRaptor(self,direction):
		for i in direction:
			if i == "U":

				value_x=self.raptorpos[0]
				value_y=self.raptorpos[1]
				self.raptorpos=[value_x-1,value_y]
				self.TheGrid[value_x][value_y] = "."
				if self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "S":
					print(">>> YOU WON!\nYou ate the Swine!")
					exit()
				elif self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "T":
					print(">>> YOU LOST!\nYou ate a Trinitrotoluene")
					exit()
				else:
					self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] = "R"
			if i == "D":
				value_x=self.raptorpos[0]
				value_y=self.raptorpos[1]
				self.raptorpos=[value_x+1,value_y]
				self.TheGrid[value_x][value_y] = "."
				if self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "S":
					print(">>> YOU WON!\nYou ate the Swine!")
					exit()
				elif self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "T":
					print(">>> YOU LOST!\nYou ate a Trinitrotoluene")
					exit()
				else:
					self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] = "R"
			if i == "R":
				value_x=self.raptorpos[0]
				value_y=self.raptorpos[1]
				self.raptorpos=[value_x,value_y+1]
				self.TheGrid[value_x][value_y] = "."
				if self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "S":
					print(">>> YOU WON!\nYou ate the Swine!")
					exit()
				elif self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "T":
					print(">>> YOU LOST!\nYou ate a Trinitrotoluene")
					exit()
				else:
					self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] = "R"
			if i == "L":
				value_x=self.raptorpos[0]
				value_y=self.raptorpos[1]
				self.raptorpos=[value_x,value_y-1]
				self.TheGrid[value_x][value_y] = "."
				if self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "S":
					print(">>> YOU WON!\nYou ate the Swine!")
					exit()
				elif self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] == "T":
					print(">> YOU LOST!\nYou ate a Trinitrotoluene")
					exit()
				else:
					self.TheGrid[self.raptorpos[0]][self.raptorpos[1]] = "R"
grid = Grid()
raptor = Raptor()
grid.printgrid()
while raptor.Lost == False:
	moves=int(input(">>> How many moves: "))
	for _ in range(moves):
		raptor.addMoves(input(">>> Move L/R/U/D: ").upper())
	print(">>> Moves: " + str(raptor.getMoves()).replace("[","").replace("\'","").replace(",","").replace("]",""))
	grid.moveRaptor(raptor.getMoves())
	grid.printgrid()
	raptor.clearMoves()
