#Displays the number of lines and characters in a text file
count=0
file=input("Please enter the filename, which must be in the same folder: ")
data = open(file, 'r')
for letter in data:
    count=count+1

with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
print("number of lines: ",count,"\n","number of characters",len(data))
