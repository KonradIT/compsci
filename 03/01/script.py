#Input two words, if those two words are found in the same line of a text.txt that line is printed
file=open("text.txt")
word_one=input("Enter the first word: ")
word_two=input("Enter the second word: ")
for line in file:
	if word_one and word_two in line:
		print(line)
file.close()

#writes to file in a new line every time
file = open("text.txt","w")
print("CTRL + C to exit")
while True:
	file.writelines('\n' + input("Enter the text: "))
file.close()

#Extension

studentMark = [1,2,3,4]
total=0
for index in range(0,len(studentMark)):
	total=total+studentMark[index]
print(studentMark)
print("Total marks: ", total)
