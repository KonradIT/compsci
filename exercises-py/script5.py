appendMe = "New bit of information\n"
appendFile = open("test.txt", "a")
appendFile.write(appendMe)
appendFile.close()
