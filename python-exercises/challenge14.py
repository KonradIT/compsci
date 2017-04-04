#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
board = []
pl = ['Player', 'Knight']
game_over = False
v_player_data = [[], []] #First array: coordinates
vh_player_data = ["",""]
for i in range(5):
	board.append([' ', ' ', ' ', ' ',' '])
def display_board():
	if player_data("Knight") == player_data("Player"):
		print("Game over!\nThe Dark Knight ALWAYS rises!")
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

def no_trail(trail):
	board[player_data(trail)[0]][player_data(trail)[1]] = " "

def get_possible_moves(w):
	message=" "
	if w == "Player":
		if vh_player_data[p2i(w)] == "":
			message="LEFT/RIGHT/UP/"
		if vh_player_data[p2i(w)] == "v":
			message = message + "LEFT/RIGHT/"
		if vh_player_data[p2i(w)] == "h":
			message = message + "UP/"
			if not player_data(w)[0] == 4:
				#cant go down when you're on the bottom.
				message = message + "DOWN/"
	else:
		#dark knight can move as he pleases.
		message="LEFT/RIGHT/UP/DOWN"
	return message

#initial setup for dark knight:
player_data("Knight",[0,0])
set_player_data("Knight")

player_data("Player",[4,4])
set_player_data("Player")

display_board()

while game_over == False:
    for i in pl:
        participant = input(">> " + i + ': Enter your move [' + get_possible_moves(i) + ']: ').upper()
        if participant == 'U':
            print(">> UP")
            vh_player_data[p2i(i)] = "v"
            no_trail(i)
            print(player_data(i)[0])
            print(player_data(i)[1])
            player_data(i,[player_data(i)[0]-1 , player_data(i)[1]])
            set_player_data(i)
        elif participant == 'D':
            print(">> DOWN")
            vh_player_data[p2i(i)] = "v"
            no_trail(i)
            print(player_data(i)[0])
            print(player_data(i)[1])
            player_data(i,[player_data(i)[0]+1 , player_data(i)[1]])
            set_player_data(i)
        elif participant == 'L':
            print(">> LEFT")
            vh_player_data[p2i(i)] = "h"
            no_trail(i)
            print(player_data(i)[0])
            print(player_data(i)[1])
            player_data(i,[player_data(i)[0] , player_data(i)[1]-1])
            set_player_data(i)
        elif participant == 'R':
            print(">> RIGHT")
            vh_player_data[p2i(i)] = "h"
            no_trail(i)
            print(player_data(i)[0])
            print(player_data(i)[1])
            player_data(i,[player_data(i)[0] , player_data(i)[1]+1])
            set_player_data(i)
        elif participant == 'Q':
            exit()
        display_board()
