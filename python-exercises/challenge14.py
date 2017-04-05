#!/usr/bin/python
# -*- coding: utf-8 -*-
#license: https://www.gnu.org/licenses/agpl-3.0.en.html
import random, os
board = []
pl = ['Player', 'Knight']
game_over = False
v_player_data = [[], []] #First array: coordinates
vh_player_data = ["",""]
log_f=True
for i in range(5):
	board.append([' ', ' ', ' ', ' ',' '])
def display_board():
	if player_data("Knight") == player_data("Player"):
		print("=====================================")
		print("== Game over! ==\n== The Dark Knight ALWAYS rises! ==")
		print("=====================================")
		set_term_color("End")
		game_over=True
		exit()
	if player_data("Player") == [0,0]:
		print("PLAYER WON!\nLooks like the Dark Knight is not so good after all...")
		set_term_color("End")
		game_over=True
		exit()
	for col in board:
		print(str(col).replace(',', ''))

def p2i(participant):
	if participant == pl[0]:
		return 0
	else:
		return 1
def player_data(participant, data=''):
    if data == '':
        # Get player data
        return v_player_data[p2i(participant)]
    else:
        # Set player data
        v_player_data[p2i(participant)] = data
def set_player_data(participant):
	pl_char = ""
	if p2i(participant) == 0:
		pl_char = "P"
	else:
		pl_char = "K"
	board[player_data(participant)[0]][player_data(participant)[1]] = pl_char

def set_finish_beacon(pos):
	board[pos[0]][pos[1]] = "Z"
def no_trail(trail):
	board[player_data(trail)[0]][player_data(trail)[1]] = " "

def get_possible_moves(w):
	message=" "

	if w == "Player":
		if vh_player_data[p2i(w)] == "":
			message="UP/"
			if player_data(w)[1] == 0:
				#Edges
				message = message + "RIGHT/"
			elif player_data(w)[1] == 4:
				#Edges
				message = message + "LEFT/"
			else:
				message = message + "LEFT/RIGHT"
		if vh_player_data[p2i(w)] == "v":
			if player_data(w)[1] == 0:
				#Edges
				message = message + "RIGHT/"
			elif player_data(w)[1] == 4:
				#Edges
				message = message + "LEFT/"
			else:
				message = message + "LEFT/RIGHT"
		if vh_player_data[p2i(w)] == "h":
			message = message + "UP/"
			if not player_data(w)[0] == 4:
				#cant go down when you're on the bottom.
				message = message + "DOWN/"
	else:
		#dark knight can move as he pleases.
		message="LEFT/RIGHT/UP/DOWN"
	return message

def set_term_color(participant):
	if participant == "Knight":
		if os.name == "nt":
			os.system('color 04')
	if participant == "Player":
		if os.name == "nt":
			os.system('color 06')
	if participant == "End":
		if os.name == "nt":
			os.system('color 07')

def log2file(participant, move, coordinates):
	if log_f == True:
		file = open('gameplay.log', 'a')
		file.write('>>'+ participant +" - " + move + " = " + str(coordinates) + '\n')
		file.close()
#initial setup for dark knight:
set_finish_beacon([0,0])

player_data("Player",[4,4])
set_player_data("Player")

player_data("Knight",[0,1])
set_player_data("Knight")
display_board()

def set_move(text, direction, i, participant, pos):
	print(">> " + text)
	log2file(i, participant, [pos[0], pos[1]])
	vh_player_data[p2i(i)] = direction
	no_trail(i)
	print(player_data(i)[0])
	print(player_data(i)[1])
	player_data(i,[pos[0],pos[1]])
	set_player_data(i)
while game_over == False:
    for i in pl:
        set_term_color(i)
        participant = input(">> " + i + ': Enter your move [' + get_possible_moves(i) + ']: ').upper()
        if participant == 'U':
            set_move("UP", "v", i, participant, [player_data(i)[0]-1 , player_data(i)[1]])
        elif participant == 'D':
            set_move("DOWN", "v", i, participant, [player_data(i)[0]+1 , player_data(i)[1]])
        elif participant == 'L':
            set_move("LEFT", "h", i, participant, [player_data(i)[0], player_data(i)[1]-1])
        elif participant == 'R':
            set_move("RIGHT", "h", i, participant, [player_data(i)[0], player_data(i)[1]+1])
        elif participant == 'Q':
            exit()
        display_board()
