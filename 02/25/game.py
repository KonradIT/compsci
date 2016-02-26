#The game
import random
def game():
  randomInt=random.randint(1,9)
  print("Guess the number!")
  guess=int(input("user@host: "))
  if (randomInt==guess):
    print("Congratulations!\nYou have a prize waiting!\nJust give your Western Union account to the Prince of Nigeria who will personally email you now")
  else:
    print("Uh, try again!")
    game()
    
if __name__ == "__main__":
  game()
