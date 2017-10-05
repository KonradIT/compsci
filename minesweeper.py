### IN CASE OF LEAKS ###
### LICENSE: https://www.gnu.org/licenses/agpl-3.0.txt ###


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
		self.print_board()
		if w == 8:
			for _ in range(int(w/2)):
				self.__Board[random.randint(0,w-1)][random.randint(0,h-1)] = "t"
		if w == 16:
			for _ in range(int(w/2)):
				self.__Board[random.randint(0,w-1)][random.randint(0,h-1)] = "t"

	def print_board(self):
		count=0
		arr=[]
		for i in self.__Board:
			count += 1
			arr.append(count)
		arr2=[]
		for i in arr:
			if len(str(i)) == 1:
				arr2.append(str(i)+" ")
			else:
				arr2.append(str(i)+"")	
		print("   " + str(arr2).replace(",","").replace("[","").replace("]","").replace("'",""))
		for index, i in enumerate(self.__Board):
			if len(str(index+1)) == 1:
				print(str(index+1) + "  " + str(i).replace(",","").replace("[","").replace("]","").replace("\'","").replace("t",".").replace(" ", "  "))
			else:
				print(str(index+1) + " " + str(i).replace(",","").replace("[","").replace("]","").replace("\'","").replace("t",".").replace(" ", "  "))

	def shoot(self):
		dots = 0
		for i in self.__Board:
			for i2 in i:
				if i2 == ".":
					dots += 1
		if dots == 0:
			print("You won!")
			exit()
		shoot_w = int(input(">>> H: "))-1
		shoot_h = int(input(">>> W: "))-1
		if self.__Board[shoot_w][shoot_h] == "t":
			print("Game over.")
			exit()
		if self.__Board[shoot_w][shoot_h] == "O":
			print("Square already blown up!")
			self.shoot()
		else:
			self.__Board[shoot_w][shoot_h] = "O"
			for i in range(2):
				print(i)
				i = i + 1
				if shoot_w+1 == self.__w:
					i = 0
				if shoot_h+1 == self.__h:
					i = 0
				if self.__Board[shoot_w][shoot_h-i] == ".":
					#print("debug")
					self.__Board[shoot_w][shoot_h-i] = "O"
				if self.__Board[shoot_w][shoot_h+i] == ".":
					#print("debug")
					self.__Board[shoot_w][shoot_h+i] = "O"
				if self.__Board[shoot_w-i][shoot_h] == ".":
					#print("debug")
					self.__Board[shoot_w-i][shoot_h] = "O"
				if self.__Board[shoot_w+i][shoot_h] == ".":
					#print("debug")
					self.__Board[shoot_w+i][shoot_h] = "O"
				if self.__Board[shoot_w+i][shoot_h+i] == ".":
					#print("debug")
					self.__Board[shoot_w+i][shoot_h+i] = "O"
				if self.__Board[shoot_w-i][shoot_h-i] == ".":
					#print("debug")
					self.__Board[shoot_w-i][shoot_h-i] = "O"
				if self.__Board[shoot_w-i][shoot_h+i] == ".":
					#print("debug")
					self.__Board[shoot_w-i][shoot_h+i] = "O"
				if self.__Board[shoot_w+i][shoot_h-i] == ".":
					#print("debug")
					self.__Board[shoot_w+i][shoot_h-i] = "O"
			self.print_board()
			
	
	def cheat(self):
		count=0
		arr=[]
		for i in self.__Board:
			count += 1
			arr.append(count)
		arr2=[]
		for i in arr:
			if len(str(i)) == 1:
				arr2.append(str(i)+" ")
			else:
				arr2.append(str(i)+"")	
		print("   " + str(arr2).replace(",","").replace("[","").replace("]","").replace("'",""))
		for index, i in enumerate(self.__Board):
			if len(str(index+1)) == 1:
				print(str(index+1) + "  " + str(i).replace(",","").replace("[","").replace("]","").replace("\'","").replace(" ", "  "))
			else:
				print(str(index+1) + " " + str(i).replace(",","").replace("[","").replace("]","").replace("\'","").replace(" ", "  "))
	def help(self):
		print("{minesweeper}.print_board() - prints board.")
		print("{minesweeper}.shoot() - shoots to square.")

	def select_dificulty(self):
		print(" __  __ _  ")                                                 
		print("|  \/  (_)_ __   ___  _____      _____  ___ _ __   ___ _ __ ")
		print("| |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|")
		print("| |  | | | | | |  __/\__ \\ V  V /  __/  __/ |_) |  __/ |   ")
		print("|_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   ")
		print("                                           |_|      ")

		print("C H O O S E Y O U R D I F F I C U L T Y L E V E L")
		print("\t[ ] 1 - Easy (8x8)\n\t[ ] 2 - Medium (16x16)")
		choice=int(input("\t>>> "))
		if choice == 1:
			print("run {minesweeper}.help() to get help.")
			self.start_game(8,8)
		if choice == 2:
			print("run {minesweeper}.help() to get help.")
			self.start_game(16,16)

