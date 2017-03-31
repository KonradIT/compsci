withdrawal = int(input("Money to withdraw)"))
if withdrawal % 10 == 0:
  Fifties = withdrawal // 50
  print (str(Fifties) + " $50 notes")
  Twenties = withdrawal % 50 // 20
  print (str(Twenties) + " $20 notes")
  Tens = withdrawal % 50 % 20 // 10
  print (str(Tens) + " $10 notes")
else:
  print("You did not enter a multiple of 10")
