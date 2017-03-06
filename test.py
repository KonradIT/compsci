"""
temp = 0
def Temperature():
    temp = int(input("Enter temperature: "))
    assert temp > 0, "Too cold"

Temperature()
"""


###############

number = float(input("Please enter a number: "))
if number < 0: #flipped >
    print("You entered a negative number")
elif number > 0: #flipped <
    print("You entered a positive number")
else:
    print("You entered zero")


###############

def stub(str):
    print(str)
    return str
if stub("hello") == "hello":
    print("passed test")
else:
    print("didnt pass test")

###############

def sum(x,y):
    return x+y
if sum(4,4) == 8:
    print("passed test")

A=input("A: ")
B=input("B: ")
C=input("C: ")
if A > B:
    if A > C:
        print("A is the biggest number")
    else:
        print("C is the biggest number")
else:
    if A >= C:
        print("B is the biggest number")
    else:
        if B >= C:
            print("C is the bigger number")

count = 1
number = int(input("Please enter a number: "))
while count < 5:
    count = count + 1
    number = int(input("Please enter a number: "))
print("Five numbers entered")
