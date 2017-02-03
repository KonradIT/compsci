import random
import string
import msvcrt

def char_no_enter():
    print("      ANSWER: ")
    input_char = msvcrt.getch().upper()
    input_char_decoded = input_char.decode("utf-8")
    return input_char_decoded
print(char_no_enter())
