#The game
import random
count = 0
def game():
  randomInt=random.randint(1,9)
  global count
  print("Guess the number!\nNumber of tries:",count)
  guess=int(input("user@host: "))
  if (randomInt==guess):
    print("Congratulations!\nYou have a prize waiting!\nJust give your Western Union account to the Prince of Nigeria who will personally email you now")
  else:
    print("Uh, try again!")
    count=count+1
    game()
    
if __name__ == "__main__":
  game()
