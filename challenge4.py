import random
import sys, time, msvcrt

def readInput( caption, default, timeout = 5):
    start_time = time.time()
    sys.stdout.write('%s(%s):'%(caption, default));
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche()
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) >= 32: #space_char
                input += chr
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print('')  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default

def introScreen():
  print("You are in a new building")
  print("In front of you are entrances to three corridors")
  print("Go down two of these corridors, and you'll end up slipping on a floor being mopped")
  print("One of these corridors though will lead to the exit - freedom!")
  print("*****Let the guessing begin!******")

def corridorPick():
  corridor =0
  while corridor != '1' and corridor != '2' and corridor != '3':
    print("Pick a corridor! 1, 2 or 3")
    corridor = int(readInput("enter: ","1"))

  return corridor
def goDownCorridor(chosenCorridor):
  print("Down the corridor we go...")
  time.sleep(3)
  exitCorridor = random.randint(1, 3)

  if chosenCorridor == str(exitCorridor):
    print("You're out!")
  else:
    print("Oh dear, you slipped and banged your head!")

anotherGo = "yes"
while anotherGo == "yes" or anotherGo == "y":
  introScreen()
  corridorNumber = corridorPick()
  goDownCorridor(corridorNumber)

  print("Another go? (y or n)")
  anotherGo = input()
