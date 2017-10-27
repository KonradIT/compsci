class Pig():
	def __init__(self, xpos, ypos):
		print("The pig")


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
	def printgrid(self):
		for i in self.TheGrid:
			print(str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
grid = Grid()
grid.printgrid()
