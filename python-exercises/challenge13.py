import sys
print("	CASH MACHINE")
amt_to_withdraw = 0
if not str(sys.argv[1]) == "":
      amt_to_withdraw=int(sys.argv[1])
else:
      amt_to_withdraw = int(input("Money to withdraw: "))
if amt_to_withdraw % 10 == 0 and amt_to_withdraw <= 500:
      bill_50 = amt_to_withdraw // 50
      for i in range(0, bill_50):
            print ("	[  50  ] ")
      if bill_50 > 0:
            print ("	" + str(bill_50) + " notes.\n")
      bill_20 = amt_to_withdraw % 50 // 20
      for i in range(bill_20):
            print ("	[  20  ] ")
      if bill_20 > 0:
            print("	" + str(bill_20) + " notes.\n")
      bill_10 = amt_to_withdraw % 50 % 20 // 10
      for i in range(bill_10):
            print ("	[  10  ] ")
      if bill_10 > 0:
            print("	" + str(bill_10) + " notes.\n")
else:
      print("There is an error.")
      print("Maximum amount is $500") if amt_to_withdraw > 500 else print("Only multiples of 10")
