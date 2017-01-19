"""
THE CHASE

A quiz game comprising of random questions given to the player who competes with the chaser. When the player answers a question correctly, they move 1 space away from the computer (the chaser). When the chaser answers the question correctly, they move a step closer to the player. If the chaser catches the player, the player loses and the game is over.

Two ways to create your Python game version of The Chase:

1) Player and Chaser take it in turns to If the player reaches a finish line after a certain number of questions answered correctly, without being caught by the chaser, the player has won
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

import random

print("_______ _    _ ______    _____ _    _           _____ ______ ")

print("|__   __| |  | |  ____|  / ____| |  | |   /\    / ____|  ____|")

print("  | |  | |__| | |__    | |    | |__| |  /  \  | (___ | |__   ")

print("  | |  |  __  |  __|   | |    |  __  | / /\ \  \___ \|  __|  ")

print("  | |  | |  | | |____  | |____| |  | |/ ____ \ ____) | |____ ")

print("  |_|  |_|  |_|______|  \_____|_|  |_/_/    \_\_____/|______|")
print("")
class Player():
    def __init__(self):
        self._steps = 0
        self._money=0
class Chaser():
    def __init__(self):
        self._steps = 0
        self._money = 0

Chaser._steps = 4
print(Chaser._steps)
