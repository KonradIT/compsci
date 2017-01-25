"""
THE CHASE

A quiz game comprising of random questions given to the player who competes with the chaser. When the player answers a question correctly, they move 1 space away from the computer (the chaser). When the chaser answers the question correctly, they move a step closer to the player. If the chaser catches the player, the player loses and the game is over.

Two ways to create your Python game version of The Chase:

1) Player and Chaser take it in turns to play. If the player reaches a finish line after a certain number of questions answered correctly, without being caught by the chaser, the player has won
At the start of the game, the player can chose to move a step closer to or further from the chaser of remain 3 spaces in front depending on the size of the prize money they wish to play for; more money the closer the player starts to the chaser.
2) Player goes first to answer as many questions as they can in a time limit. The chaser then takes a turn to answer the same number of questions as the player in a time limit. As a bonus, the player can start 3 places (equivalent to 3 correct answers) ahead of the chaser. If the chaser fails to answer the same number of questions as the player within the time limit, the player has won.

"""

"""
MIT License:
Copyright 2017 Konrad Iturbe
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#TODO
# [ ] Add colors (?)
# [ ] Add big text
# [ ] add fonts
# [ ] add timer

import random
import sys
print("THE CHASE")
PLAYER_STEPS=0
CHASER_STEPS=0
PLAYER_CASH=0
CHASER_CASH=0
questionArray =["Who is/was the President of the United States of America during 2017 - 2025?","In what year was YouTube founded?","Where was the first iPhone unveiled?","What is the capital of Uganda?", "What is 38^7-100 ?"]
answersArray=[["A: Gordon Ramsey","B: Donald J. Trump","C: Leonardo DiCaprio","D: Rick Astley"],["A: 2006","B: 2016","C: 1969","D: 2005"],["A: Helsinki","B: San Francisco","C: New York","D: Miami"],["A: Freetown","B: Nairobi","C: Kigali","D: Kampala"],["A: 215526793728","B: 114415582492","C: 114415582491","D: 114415586492"]]
answersNumber=["B","A","B","D","A"]
deck = list(range(1, 4))
random.shuffle(deck)
playerPlayed=False
while playerPlayed == False:
    print("Player:")
    questionRandom=deck.pop()
    print(questionArray[questionRandom])
    print(answersArray[questionRandom])
    playerAnswer=input("Enter your Answer: ").upper()
    if(playerAnswer==answersNumber[questionRandom]):
        PLAYER_STEPS += 1
        print("Congratulations! You moved 1 step, you're " + str(PLAYER_STEPS - CHASER_STEPS) + " steps away from the chaser.")
        playerPlayed=True
    else:
        print("WRONG!!!")
        playerPlayed=True
while playerPlayed == True:
    print("Chaser:")
    questionRandom=deck.pop()
    print(questionArray[questionRandom])
    print(answersArray[questionRandom])
    chaserAnswer=input("Enter your Answer: ").upper()
    if(chaserAnswer==answersNumber[questionRandom]):
        CHASER_STEPS += 1
        if PLAYER_STEPS <= CHASER_STEPS:
            print("PLAYER YOU LOST!!!!")
            sys.exit(0)
        print("Catching up! Player beware, the chaser is just " + str(PLAYER_STEPS - CHASER_STEPS) + " steps shy!")
        playerPlayed=False
