import csv

def menu():
	print("\nOPTION A\tStatics for specific player")
	print("\nOPTION B\tStatics for specific player")
	print("\nOPTION C\tStatics for specific player")
	validOption = False
	while validOption == False:
		option = input("\nEnter A, B, C or Q: ")
		if option.upper() == "A":
			validOption=True
			optionA()
		else: 
			if option.upper() == "B":
				validOption=True
				optionB()
			else: 
				if option.upper() == "C":
					validOption=True
					optionC()
				else: 
					if opion.upper() == "D":
						validOption=True
						#optionD()
						exit()
					else:
						print("Enter a correct letter")
	menu()

def optionA():
	print("Enter a ID: ")
	userID = input("\nID: ")
	validA=False
	for row in playerList:
		if row[0]==playerId:
			validA=True
			print("\nThe stats for",playerId,"are:")
			print("*"*75)
			print("\t",row[1],"\t\t",row[2])
