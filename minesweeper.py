import random
import time
import subprocess
class MineSweeper:
	def __init__(self):
		self.__Board = []
		self.select_dificulty()

	def start_game(self, w,h):
		self.__w=w
		self.__h=h
		self.__Board = [["." for x in range(w)] for y in range(h)]
		for i in self.__Board:
			print(str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))
		if w == 8:
			for _ in range(int(w/2)):
				self.__Board[random.randint(0,w-1)][random.randint(0,h-1)] = "t"
		if w == 16:
			for _ in range(int(w/2)):
				self.__Board[random.randint(0,w-1)][random.randint(0,h-1)] = "t"
		if w == 30:
			for _ in range(int(w/2)):
				self.__Board[random.randint(0,w-1)][random.randint(0,h-1)] = "t"

	def print_board(self):
		count=0
		arr=[]
		for i in self.__Board:
			count += 1
			arr.append(count)
		print("   " + str(arr).replace(",","").replace("[","").replace("]","").replace(" ", "  "))
		for index, i in enumerate(self.__Board):
			print(str(index+1) + "  " + str(i).replace(",","").replace("[","").replace("]","").replace("\'","").replace("t",".").replace(" ", "  "))

	def shoot(self):
		shoot_w = int(input(">>> W: "))-1
		shoot_h = int(input(">>> H: "))-1
		if self.__Board[shoot_w][shoot_h] == "t":
			print("Game over.")
			exit()
		else:
			if self.__w == 8:
				for _ in range(int(self.__w/2)):
					self.__Board[random.randint(0,self.__w-1)][random.randint(0,self.__h-1)] = "O"
			if self.__w == 16:
				for _ in range(int(self.__w/2)):
					self.__Board[random.randint(0,self.__w-1)][random.randint(0,self.__h-1)] = "O"
			if self.__w == 30:
				for _ in range(int(self.__w/2)):
					self.__Board[random.randint(0,self.__w-1)][random.randint(0,self.__h-1)] = "O"
			self.print_board()
			
	
	def cheat(self):
		for i in self.__Board:
			print(str(i).replace(",","").replace("[","").replace("]","").replace("\'",""))

	
	def select_dificulty(self):
		print(" __  __ _  ")                                                 
		print("|  \/  (_)_ __   ___  _____      _____  ___ _ __   ___ _ __ ")
		print("| |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|")
		print("| |  | | | | | |  __/\__ \\ V  V /  __/  __/ |_) |  __/ |   ")
		print("|_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   ")
		print("                                           |_|      ")

		print("C H O O S E Y O U R D I F I C U L T Y L E V E L")
		print("\t[ ] 1 - Easy (8x8)\n\t[ ] 2 - Medium (16x16)\n\t[ ] 3 - Hard (30x10)")
		choice=int(input("\t>>> "))
		if choice == 1:
			self.start_game(8,8)
		if choice == 2:
			self.start_game(16,16)
		if choice == 3:
			self.start_game(30,10)