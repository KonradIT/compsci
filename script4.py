filename = input("Where would you like to save it (give full location): ")
newText=""
line = input("Please insert your shopping list:\n")
while line != "":
    newText = (newText + line + "\n")
    line = input("Anything else? Press Enter to skip: ")
textFile = open(filename,"w")
textFile.write(newText)
textFile.close()
