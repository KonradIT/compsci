import time
print("##################")
print("# Gym Membership #")
print("##################")
time.sleep(3)
print("Processing...")
time.sleep(1)
print("")
name=input("Whats your name: ")
surname=input("Whats your surname: ")
print("Hi, " + name + " " + surname)
time.sleep(2)
gender=input("Whats your sex: ")
if gender == "M":
   print ("Male!")
elif gender == "F":
   print ("Female!")
else:
   print ("u wot m8")
validAge = 0
while validAge == 0:
	try:
   		age=int(input("Enter your age: "))
	except ValueError:
   		print("Please input a valid age: ")
   		continue
	else:
   		break

validWeight = 0
while validWeight == 0:
	try:
   		weight=int(input("Enter your weight in KG: "))
	except ValueError:
   		print("Please input a valid weight: ")
   		continue
	else:
   		break
time.sleep(4)
print("Loading...")
time.sleep(4)
print("Name: " + name)
print("Surname: " + surname)
time.sleep(3)
print("Saving...")
time.sleep(2)
print("Hang tight!")
time.sleep(4)
print("All your data has been saved!")
