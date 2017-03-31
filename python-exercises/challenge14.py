print("THE INCREDIBLE GAME")
board=[
	["", "", ""],
	["", "", ""],
	["", "", ""]
]
def display_board():
	for i in board:
		print(str(i).replace(",",""))
display_board()
