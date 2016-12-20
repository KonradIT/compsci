numberList = [10,16,40,8]
def serial_search():
	y = input("Enter the number: ")
	for x in numberList:
		if x == int(y):
			print("Match found!")
serial_search()
