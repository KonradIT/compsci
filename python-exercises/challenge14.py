import random
board=[[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "]]
pl=["Player","Knight"]
game_over=False
def display_board(knight_pos, player_pos):
    board[knight_pos.index("K")][knight_pos.index("K")] = " "
    board[player_pos[0]][player_pos[1]] = "P"
    board[knight_pos[0]][knight_pos[1]] = "K"
    if board[knight_pos[0]][knight_pos[1]] == board[player_pos[0]][player_pos[1]]:
        print("Game over")
        game_over=True
    else:
        for col in board:
            print(str(col).replace(",",""))
while game_over == False:
    for i in pl:
        player=input(i + ": Enter your move: ")
        display_board([random.randint(0,3),random.randint(0,3)],[1,3])
        
