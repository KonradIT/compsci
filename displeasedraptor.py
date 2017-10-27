import random
class Raptor():
	def __init__(self):
		print(">>> Attacks the swine")
		self.Lost = False
		self.Moves = []
	def addMoves(self):
		self.Moves.append(move)
	def getMoves(self):
		return self.Moves

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
		raptorpos=[]
		self.TheGrid[random.randint(0,5)][random.randint(0,9)] = "T"
		self.TheGrid[random.randint(0,5)][random.randint(0,9)] = "S"
		raptorpos = [random.randint(0,5),random.randint(0,9)]
		self.TheGrid[raptorpos[0]][raptorpos[1]] = "R"

	def printgrid(self):
		for i in self.TheGrid:
			print("   " + str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
	def moveRaptor(self,direction):
		for i in direction:
			if direction == "U":
				value_x=raptorpos[0]
				value_y=raptorpos[1]
				raptorpos=[value_x-1,value_Y]
				self.TheGrid[raptorpos[0]][raptorpos[1]] = "R"
				self.printgrid()
grid = Grid()
raptor = Raptor()
grid.printgrid()
while raptor.Lost == False:
	moves=int(input(">>> How many moves: "))
	for _ in range(moves):
		raptor.moves(input(">>> Move L/R/U/D: ").upper())
		raptor.moves()
	grid.moveRaptor(raptor.moves())
