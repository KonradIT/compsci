#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
board = [[' ', ' ', ' ', ' ',' '], [' ', ' ', ' ', ' ',' '], [' ', ' ', ' ', ' ',' '], [' ', ' ', ' ', ' ',' '], [' ', ' ', ' ', ' ',' ']]
pl = ['Player', 'Knight']
game_over = False
v_player_data = [[], []] #First array: coordinates

def display_board(player_pos):
	for col in board:
		print(str(col).replace(',', ''))


def player_data(player, data=''):
    if data == '':
        # Get player data
        return v_player_data[player]
    else:
        # Set player data
        v_player_data[player] = data

while game_over == False:
    for i in pl:
        player = input(i + ': Enter your move [U/D/L/R]: ').upper()
        if player == 'U':
            print("UP")
        elif player == 'D':
            print("DOWN")
        elif player == 'L':
            print("LEFT")
        elif player == 'R':
            print("RIGHT")
        last_coordinates = [1, 2]
        display_board(i)
