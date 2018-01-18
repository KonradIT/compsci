## Big Break 
import random
import time
class BigBreak:
	def __init__(self):
		print("  ____  _         ____                 _    ")
		time.sleep(0.5)
		print(" |  _ \(_)       |  _ \               | |   ")
		time.sleep(0.5)
		print(" | |_) |_  __ _  | |_) |_ __ ___  __ _| | __")
		time.sleep(0.5)
		print(" |  _ <| |/ _` | |  _ <| '__/ _ \/ _` | |/ /")
		time.sleep(0.5)
		print(" | |_) | | (_| | | |_) | | |  __/ (_| |   < ")
		time.sleep(0.5)
		print(" |____/|_|\__, | |____/|_|  \\___|\\__,_|_|\\_\\")
		time.sleep(0.5)
		print("           __/ |                            ")
		time.sleep(0.5)
		print("          |___/                             ")
		time.sleep(1)
		print("Loading...")
		time.sleep(1)
		print("$$$ You will now choose a color of the ball to try to put in the corresponding pocket")
		print("$$$ Then based on the choice a question will be presented.")
		self.questions=[
						[
							["What's the capital of sweden","stockholm"],
							["What's the capital of spain","madrid"],
							["largest river...","amazon"],
							["What is the capital of Uganda", "kampala"]
						],
						[
							["Who won the US Presidential election in 2016","donald trump"],
							["In what year was YouTube founded","2005"],
							["Where was the first iPhone unveiled?","san francisco"],
							["2+2-1","3"]
						]
						]
		self.questionsAnswered=0
		self.tries=0
	def ready(self,section):
		self.questionsAnswered += 1
		print("Question time!")
		q=random.randint(0,3)
		print("$$$ %s ?" % self.questions[section][q][0])
		if str(input("$$$ ANS: ")).lower() == self.questions[section][q][1]:
			print("Correct Answer!!!")
		else:
			if self.tries < 2:
				self.tries += 1
				self.ready(section)
			else:
				self.tries=0
class SnookerPlayer:
	def __init__(self):
		self.countdown=30
		self.cash=0
		self.section=1000
		self.outcome=True
	def shoot(self):
		
		print("Money: %s\nCountdown: %s" % (self.cash, self.countdown))
		print("$$$ Colors:\n\nGeography:\n\t[R]ed\n\t[C]yan\n\t[G]reen\n\nMisc.\n\t[B]lack\n\t[Y]ellow\n\t[P]urple")
		color = input("$$$ What color? ").upper()
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
				print("Yellow.... 40$ for you.")
			elif color == "P":
				self.cash += 120
				print("Purple.... 120$ for you.")
			self.outcome=True
		else:
			print("Too hard, try again next time.")
			self.outcome=False
			time.sleep(2)
		self.countdown -= 3
game = BigBreak()
player = SnookerPlayer()
while player.countdown > 0:
	player.shoot()
	if player.outcome == False:
		game.ready(player.section)
print("You won %s $" % player.cash)
