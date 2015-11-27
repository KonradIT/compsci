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
def optionB():
	validB=False
	while validB==False:
		goalsOrAssists = input("\nPlease enter 'goals' or 'assists': ")
		if goalsOrAssists.lower()=="goals" or goalsOrAssists.lower()=="assists":
			validB=True
		else:
			print("Invalid entry")
	print("\n\t\tStats\n\t\t\t")
	print("*"*75)
	if goalsOrAssists.lower()=="goals":
		print("\tPlayer ID \tNo. Goals")
	else:
		print("\tPlayer ID \tNo. Assists")
	for row in playerList:
		if row[1].lower()==goalsOrAssists.lower():
			print("\t",row[0],"\t\t",row[2])
		elif row[3].lower()==goalsOrAssists.lower():
			print("\t",row[0],"\t\t",row[4])
	print("*"*75)
def optionC():
	goalsList=[]
	assistList=[]
	for row in playerList:
		goals=int(row[2])
		goalList.append([row[0],goals])
		assists=int(row[4])
		assistList.append([row[0],assists])
		goalSorted = sorted(goalList, key = lambda col: int(col[1]), reverse=True)
	assistSorted = sorted(assistList, key = lambda col: int(col[1]), reverse=True)
	print("\nTop Goal scorer:")
	print(goalSorted[0][0],"is the top scorer this season with",goalSorted[0][1],"goals")
	if goalSorted[0][1] == goalsSorted[1][1]:
		print(goalsSorted[1][0],"is the top scorer this season with",goalsSorted[0][1],"goals")
	print("\nMost assists:")
	print(assistSorted[0][0],"has the most assists with",assistSorted[0][1],"this season")
	if assistSorted[0][1] == goalSorted[1][1]:
		print(assistSorted[1][0],"has the most assists with",assistSorted[0][1],"this season")
	if assistSorted[0] == goalsSorted[1][1]:
		print(assistSorted[1][0],"has the most assists with",assistSorted[0][1],"this season")
def importData():
	global playerList
	with open('playersRecords.txt') as f:
		reader = csv.reader(f)
		playerList = list(reader)
importData()
menu()		
