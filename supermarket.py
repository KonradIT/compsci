import random
class Supermarket:
	def __init__(self):
		self.Points=0
		self.Products=[["-||-" for x in range(5)] for y in range(5)]
		self.haswon=False
	def print_shelves(self):
		letters=["A","B","C","D","E"]
		count=0
		arr=[]
		for i in self.Products:
			count += 1
			arr.append(count)
		arr2=[]
		for i in arr:
			arr2.append(letters[i-1]+"   ")
		print("     " + str(arr2).replace(",","").replace("[","").replace("]","").replace("'",""))
		for index, i in enumerate(self.Products):
			if len(str(index+1)) == 1:
				print(str(index+1) + "  " + str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
		
	def set_clue_xy(self, 	x,y,clue):
				self.Products[x][y]="- " + clue + "-"
class Product:
	def __init__(self):
		self.Items=[
		["Apple","Burritos and _____"],
		["Doritos","Toffee and _____ go well together"],
		["Coffee","Put some _____ on that meat"],
		["Meat","The NATO needs more _____"],
		["Tomato","WON"]
		]
		self.ItemsWithClue=[[]]
	def set_clue_xy(self,x,y):
		self.ItemsWithClue.append([x,y])
market = Supermarket()
pr = Product()
for clue in range(5):
	x = random.randint(0,4)
	y = random.randint(0,4)
	if market.Products[x][y] == "-||-":
		pr.set_clue_xy(x,y)
	else:
		x = random.randint(0,4)
		y = random.randint(0,4)
		if market.Products[x][y] == "-||-":
			pr.set_clue_xy(x,y)
while market.haswon == False:

	market.print_shelves()
	input()
