import sys
print("CASH MACHINE")
amt_to_withdraw = 0
if not str(sys.argv[1]) == "":
      amt_to_withdraw=int(sys.argv[1])
else:
      amt_to_withdraw = int(input("Money to withdraw: "))
if amt_to_withdraw % 10 == 0 and amt_to_withdraw <= 500:
      bill_50 = amt_to_withdraw // 50
      for i in range(bill_50):
            print ("=	[  50  ] ")
            print ("	" + str(bill_50) + " notes.")
      bill_20 = amt_to_withdraw % 50 // 20
      for i in range(bill_20):
            print ("=	[  20  ] ")
            print("	" + str(bill_20) + " notes.")
      bill_10 = amt_to_withdraw % 50 % 20 // 10
      for i in range(bill_10):
            print ("=	[  10  ] ")
            print("	" + str(bill_10) + " notes.")
else:
      print("There is an error.")
      print("Maximum amount is $500") if amt_to_withdraw > 500 else print("Only multiples of 10")
