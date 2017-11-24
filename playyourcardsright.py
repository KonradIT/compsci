#Play Your Cards Right

import random
class CardsRight():
	def __init__(self):
		self.deck = list('23456789'*4)
		for _ in range(4):
			self.deck.append('10')
		random.shuffle(self.deck)
		self.progress=[0,0]
		print("  ____  _              __   __                  ____              _       ____  _       _     _   ")
		print(" |  _ \| | __ _ _   _  \ \ / /__  _   _ _ __   / ___|__ _ _ __ __| |___  |  _ \(_) __ _| |__ | |_ ")
		print(" | |_) | |/ _` | | | |  \ V / _ \| | | | '__| | |   / _` | '__/ _` / __| | |_) | |/ _` | '_ \| __|")
		print(" |  __/| | (_| | |_| |   | | (_) | |_| | |    | |__| (_| | | | (_| \__ \ |  _ <| | (_| | | | | |_ ")
		print(" |_|   |_|\__,_|\__, |   |_|\___/ \__,_|_|     \____\__,_|_|  \__,_|___/ |_| \_\_|\__, |_| |_|\__|")
		print("                |___/                                                             |___/           ")
		
	def play(self, id, name):
		print(self.deck)
		print("Its {} turn".format(name))
		print("Progress: " + str(self.progress[id]))
		print(self.deck[self.progress[id]])
		choice=int(input("Guess Which Card comes next: "))
		next = int(self.deck[self.progress[id+1]])
		if choice < next:
			print(choice-next)
			print("Too high!!")
		elif choice > next:
			print(next-choice)
			print("Too low!!")
		else:
			print("You guessed it!")
	
g = CardsRight()
while True:
	for index, i in enumerate(["Corry","Tofik"]):
		g.play(index,i)
		

"""
   li = [0,1,2,3]

   for i in range(len(li)):

       if i < len(li)-1:

           # until end is reached
           print 'this', li[i]
           print 'next', li[i+1]
"""
