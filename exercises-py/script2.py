filename = input("Name of file to load, e.g. File Name.txt: ")

file = open(filename,"r")
content = file.read()
file.close()

print("See below for the content of your file: ")
print(content)
