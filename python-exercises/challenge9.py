"""
CHAIN REACTION GAME:
The player has to make a set of choices to create a successful chain reaction to complete the game (you choose the context). When the player commences the chain reaction, the reaction may not complete its course if a setting is incorrect on the way. There should be at least three settings on the way. You decide how much assistance the player will have in printed text.

EXTENSIONS:
Give the player more than two options for each link in the chain
Player’s number of lives (goes) is limited; if they make too many wrong selections of choices that result in the chain not being complete, the game is over.
Multi-player; who can complete the chain first with the least number of goes/settings!

LICENSE:
    Copyright 2017 Konrad Iturbe.
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import random
import time

print("LAUNCHER JET GAME\n")
LAUNCHER_JET_RUNWAY=""
LAUNCHER_JET_TAKEOFF=""
LAUNCHER_JET_FUEL=""
def startGame():
    LAUNCHER_JET_RUNWAY=int(input("\nEnter the runway length in meters: "))
    while LAUNCHER_JET_RUNWAY < 100:
        print("ERROR: Not enough runway for the jet plane to take off. Remember: Not greater than 150.")
        LAUNCHER_JET_RUNWAY=int(input("\nEnter the runway length in meters again: "))
    print("RUNWAY:\n  " + str(LAUNCHER_JET_RUNWAY) + " meters\n  " + str(LAUNCHER_JET_RUNWAY/1000) + " KM")
    LAUNCHER_JET_FUEL=int(input("\nEnter the amount of fuel needed in liters: "))
    while LAUNCHER_JET_FUEL < 150000:
        print("ERROR: Not enough fuel!")
        LAUNCHER_JET_FUEL=int(input("\nEnter the amount of fuel needed in liters again: "))
    print("FUEL:\n  " + str(LAUNCHER_JET_FUEL) + " liters\n  " + str(round(LAUNCHER_JET_FUEL*0.26417,2)) + " gallons")
    LAUNCHER_JET_TAKEOFF=int(input("\nEnter the amount of time between runway engine start and takeoff: "))
    while LAUNCHER_JET_TAKEOFF < 10:
        print("ERROR: Not enough take off time, you'll crash with only " + str(LAUNCHER_JET_TAKEOFF) + " seconds in the runway.")
        LAUNCHER_JET_TAKEOFF=int(input("\nEnter the amount of time between runway engine start and takeoff again: "))
    print("TAKEOFF:\n  " + str(LAUNCHER_JET_TAKEOFF) + " seconds\n")
    time.sleep(2)
    print("Variables set!")
    time.sleep(1)
    print("Fuel check...")
    time.sleep(1)
    print("Passanger check...")
    time.sleep(1)
    print("Launch is go!")
    time.sleep(2)
    print("Moving jet to runway...")
    time.sleep(4)
    print("Jet in position.")
    time.sleep(2)
    print("Engine started!\nTake off in " + str(LAUNCHER_JET_TAKEOFF) + " seconds.")
    time.sleep(LAUNCHER_JET_TAKEOFF)
    print("Taking off!")
startGame()
