#Play Your Cards Right

import random
class CardsRight():
	def __init__(self):
		deck = list('23456789JQKA'*4)
		random.shuffle(deck)
		progress=[0,0]
		print("  ____  _              __   __                  ____              _       ____  _       _     _   ")
		print(" |  _ \| | __ _ _   _  \ \ / /__  _   _ _ __   / ___|__ _ _ __ __| |___  |  _ \(_) __ _| |__ | |_ ")
		print(" | |_) | |/ _` | | | |  \ V / _ \| | | | '__| | |   / _` | '__/ _` / __| | |_) | |/ _` | '_ \| __|")
		print(" |  __/| | (_| | |_| |   | | (_) | |_| | |    | |__| (_| | | | (_| \__ \ |  _ <| | (_| | | | | |_ ")
		print(" |_|   |_|\__,_|\__, |   |_|\___/ \__,_|_|     \____\__,_|_|  \__,_|___/ |_| \_\_|\__, |_| |_|\__|")
		print("                |___/                                                             |___/           ")
		
	def play(self, id, name):
		print("Its {} turn".format(name))
		print(progress[id])
	
g = CardsRight()
while True:
	for index, i in enumerate(["Corry","Tofik"]):
		g.play(index,i)
