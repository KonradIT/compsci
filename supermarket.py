import random
class Supermarket:
	def __init__(self):
		self.Points=0
		self.Products=[["-||-" for x in range(5)] for y in range(5)]
		self.haswon=False
		for i in self.Products:
			i[1] = "-|V-"
			i[2] = "-|M-"
			i[3] = "-|S-"
			i[4] = "-|D-"


	def print_shelves(self):
		count=0
		arr=[]
		for i in self.Products:
			count += 1
			arr.append(count)
		arr2=[]
		for i in arr:
			arr2.append(str(i)+"   ")
		print("     " + str(arr2).replace(",","").replace("[","").replace("]","").replace("'",""))
		for index, i in enumerate(self.Products):
			if len(str(index+1)) == 1:
				print(str(index+1) + "  " + str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
		
	def set_clue_xy(self, 	x,y,clue):
		self.Products[x][y]="- " + clue + "-"
	def increasePoints(self):
		self.Points += 1
	def addSolved(self, col):
		for i2 in self.Products:
			i2[col-1] = "-OO-"
class Product:
	def __init__(self):
		self.Items=[
		["Apple","Burritos and _____",4],
		["Doritos","Toffee and _____ go well together",5],
		["Coffee","Put some _____ on that beat",3],
		["Meat","The NATO needs more _____",2],
		["Tomato","WON"]
		]
market = Supermarket()
pr = Product()
rand= random.randint(1,5)
while market.haswon == False:
	if pr.Items[market.Points][1] != "WON":
		#print(rand)
		market.print_shelves()
		print(pr.Items[market.Points][1])
		c=int(input("Col: "))
		r=int(input("Row: "))
		if c == 99:
			print(pr.ItemsWithClue)
		if c == pr.Items[market.Points][2]:

			if r == rand:
				market.addSolved(c)
				print("***YES!!!***")
				print("Its " +  pr.Items[market.Points+1][0])
				print("BUT... \n\tA clue appeared!!")
				market.increasePoints()
				rand= random.randint(1,5)
			else:
				print("No clue. Try again!")
		else:
			print("Wrong shelf.")
	else:
		exit()