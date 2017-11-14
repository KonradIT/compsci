
class RamblingBuck:
	def __init__(self):
		self.battlefield =[[" " for x in range(2)] for y in range(5)]	
		self.battlefield[0][0] = "1"
		self.battlefield[0][1] = "2"
		self.positions=[0,0]
		self.lost=False
		self.shots = 0
	def printbattlefield(self):
		for i in self.battlefield:
			print(str(i).replace("[","").replace("]","").replace(",",""))
	def bombard(self, channel):
		print(">>> Bombarding {}".format(channel))
		self.shots += 1
		if self.shots == 10:
			print("You won.")
			exit()
		for i in self.positions:
		  if i >= 3:
		    print("You lost.")
		    exit()
		indicator=0
		opponent=0
		if channel == 1:
			opponent=1
		else:
			indicator=1
		self.battlefield[self.positions[opponent]][opponent] = " "
		self.battlefield[self.positions[indicator]][indicator] = " "
		self.positions[indicator] += 1
		self.positions[opponent] += 1
		self.battlefield[self.positions[opponent]][opponent] = " "
		self.battlefield[self.positions[opponent]+1][opponent] = str(opponent+1)
		
		if self.battlefield[self.positions[indicator]][indicator] == "X":
			self.battlefield[self.positions[indicator]][indicator] = " "
			self.positions[indicator] = 0
			self.battlefield[self.positions[indicator]][indicator] = str(channel)
		else:
			self.battlefield[self.positions[indicator]][indicator] = " "
			self.battlefield[self.positions[indicator]+1][indicator] = "X"
		
bucks = RamblingBuck()
while bucks.shots < 11:
	while bucks.lost == False:
		bucks.printbattlefield()
		ch=int(input(">>> Which channel? [1/2]: "))
		print(">>> Shots: {} - {} left.".format(bucks.shots, 10-bucks.shots))
		bucks.bombard(ch)
