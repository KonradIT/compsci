## Big Break 
import random
import time
class BigBreak:
	def __init__(self):
		print("  ____  _         ____                 _    ")
		print(" |  _ \(_)       |  _ \               | |   ")
		print(" | |_) |_  __ _  | |_) |_ __ ___  __ _| | __")
		print(" |  _ <| |/ _` | |  _ <| '__/ _ \/ _` | |/ /")
		print(" | |_) | | (_| | | |_) | | |  __/ (_| |   < ")
		print(" |____/|_|\__, | |____/|_|  \\___|\\__,_|_|\\_\\")
		print("           __/ |                            ")
		print("          |___/                             ")
		time.sleep(1)
		self.questions=[
						[
							["Whats the capital of sweden","stockholm"],
							["Whats the capital of spain","madrid"],
							["largest river...","amazon"],
							["What is the capital of Uganda?", "Kampala"]
						],
						[
							["Who won the US Presidential election in 2016?","Donald Trump"],
							["In what year was YouTube founded?","2005"],
							["Where was the first iPhone unveiled?","San Francisco"],
							["2+2-1","3"]
						]
						]
		self.questionsAnswered=0
		self.tries=0
	def ready(self,section):
		print("Question time!")
		q=random.randint(0,3)
		print(self.questions[section][q][0])
		if str(input("ANS: ")).lower() == self.questions[section][q][1]:
			print("Correct Answer!!!")
		else:
			exit()
class SnookerPlayer:
	def __init__(self):
		self.points=0
		self.cash=0
		self.section=1000
	def shoot(self):
		print("Colors:\n\nGeography:\n\t[R]ed\n\t[C]yan\n\t[G]reen\n\nMisc.\n\t[B]lack\n\t[Y]ellow\n\t[P]urple")
		color = input("What color? ")
		if color == "R" or color == "C" or color == "G":
			self.section=0
		else:
			self.section=1
		print("Aiming...")
		time.sleep(1)
		if random.randint(0,1) == 0:
			print("BALL IN POCKET!!!")
			if color == "R":
				self.cash += 10
				print("Red.... 10$ for you.")
			elif color == "C":
				self.cash += 100
				print("Cyan.... 100$ for you.")
			elif color == "G":
				self.cash += 60
				print("Green.... 60$ for you.")
			if color == "B":
				self.cash += 70
				print("Black.... 70$ for you.")
			elif color == "Y":
				self.cash += 40
				print("Yellow.... 100$ for you.")
			elif color == "P":
				self.cash += 120
				print("Purple.... 120$ for you.")
				
		else:
			print("Too hard, try again next time.")
			time.sleep(2)
game = BigBreak()
player = SnookerPlayer()
while game.tries < 8:
	player.shoot()
	game.ready(player.section)
	
