"""
WII PARTY PYTHON
By Konrad Iturbe.
LICENSE:
    Copyright 2017 Konrad Iturbe.
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
Extensions/TODO:

- Create multiplayer option; if both survive all rounds, it’s a draw.

"""
import msvcrt
import string
import random
import threading
import sys
COUNT=0
COUNT_CORRECT=0
CHOSEN_LETTER=""
QUESTIONS=7
TIMEOUT = 1
STRINGS=["nab","nae","nag","nah","nam","nan","nap","naw","nay","neb","nee","neg","net","new","nib","nil","nim","nip","nit","nix","nob","nod","nog","noh","nom","noo","nor","nos","not","now","nth","nub","nun","nus","nut"]
print("\n\nWII GAME\n-----------\nGESTURE MIRRORING WITH TIMEOUT")
print("RULES:\nYou play vs the computer\nThe computer will show you a letter OR a word\nThe point of the game is that you have less time to enter the letter or word each time.\nYou will start with 1 second - 1000ms, and each correct answer will subtract you 100ms\nYou win when you have done " + str(QUESTIONS)+" correct steps.")
def char_no_enter():
    print("      ANSWER:")
    input_char = msvcrt.getch().upper()
    input_char_decoded = input_char.decode("utf-8")
    return input_char_decoded
def readInput(caption, default, timeout):
    class KeyboardThread(threading.Thread):
        def run(self):
            self.timedout = False
            self.input = ""
            while True:
                if msvcrt.kbhit():
                    chr = msvcrt.getche()
                    if ord(chr) == 13:
                        break
                    elif ord(chr) >= 32:
                        self.input += chr.decode("utf-8")
                if len(self.input) == 0 and self.timedout:
                    break


    sys.stdout.write("%s(%s):"%(caption, default));
    result = default
    it = KeyboardThread()
    it.start()
    it.join(timeout)
    it.timedout = True
    if len(it.input) > 0:
        # wait for rest of input
        it.join()
        result = it.input
    print ("")  # needed to move to next line
    return result
while COUNT < QUESTIONS:
    input_val = ""
    CHOSEN_LETTER = ""
    if(random.randint(0,10)% 2 == 0):
        CHOSEN_LETTER=str(random.choice(string.ascii_uppercase))
        print("\n      Letter: " + CHOSEN_LETTER)
        input_val = char_no_enter()
        print("      \n" + input_val)
    else:
        CHOSEN_LETTER = STRINGS[random.randint(1,30)]
        print("\n      Word: " + CHOSEN_LETTER)
        TIMEOUT=TIMEOUT-0.10
        input_val = readInput("Enter: ", "fail",TIMEOUT).lower()
        print("      \n" + input_val)
    if input_val == CHOSEN_LETTER:
        print("\n      CORRECT!!")
        COUNT_CORRECT += 1
    else:
        if input_val == "fail":
            print("\n      TOO SLOW!!")
        else:
            print("\n      WRONG!!")
            print("\n      Correct answers: " + str(COUNT_CORRECT))
    COUNT += 1
print("\n-----------\nResults:\nMoves answered correctly: " + str(COUNT_CORRECT) + "\nMoves answered wrong: " + str(QUESTIONS - COUNT_CORRECT))
