p1totalCorrect = 0
p2totalCorrect = 0
loops = 0
import random
qsLeft = [1, 2, 3, 4, 5, 6, 7, 8]
player = True

def q1():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalorrect
    ans = str(input("Which of these countries is NOT in more than 1 continent?\nMexico, Russia, Azerbaijan or Indonesia: "))
    if str.lower(ans) == "mexico":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You were awarded 1 point\n")
        loops = loops + 1
        qsLeft.remove(1)
        player = not player
    elif str.lower(ans)=="russia" or str.lower(ans)=="azerbaijan" or str.lower(ans)=="indonesia":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(1)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q1()
def q2():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these colours is NOT part of the Panamanian flag?\nBlue, Green, White or Red: "))
    if str.lower(ans) == "green":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(2)
        player = not player
    elif str.lower(ans)=="blue" or str.lower(ans)=="white" or str.lower(ans)=="red":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(2)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q2()
def q3():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these counties was never a part of the Spanish/Portuguese empire?\nHaiti, Sri Lanka, Guyana or Equatorial Guinea: "))
    if str.lower(ans) == "guyana":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(3)
        player = not player
    elif str.lower(ans)=="haiti" or str.lower(ans)=="sri lanka" or str.lower(ans)=="equatorial guinea":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(3)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q3()
def q4():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these counties is NOT in Oceania?\nVanuatu, Palau, Samoa or Suriname: "))
    if str.lower(ans) == "suriname":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(4)
        player = not player
    elif str.lower(ans)=="vanuatu" or str.lower(ans)=="palau" or str.lower(ans)=="samoa":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(4)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q4()
def q5():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these counties has the largest population?\nCuba, Sweden, Greece or Israel: "))
    if str.lower(ans) == "cuba":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(5)
        player = not player
    elif str.lower(ans)=="sweden" or str.lower(ans)=="greece" or str.lower(ans)=="israel":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(5)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q5()

def q6():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these counties has the greatest average elevation?\nChina, Spain, Norway or Iceland: "))
    if str.lower(ans) == "china":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(6)
        player = not player
    elif str.lower(ans)=="spain" or str.lower(ans)=="norway" or str.lower(ans)=="iceland":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(6)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q6()

def q7():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these is NOT the capital of an Asian country? Pyongyang, Amman, Managua or Bishkek: "))
    if str.lower(ans) == "managua":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(7)
        player = not player
    elif str.lower(ans)=="pyongyang" or str.lower(ans)=="amman" or str.lower(ans)=="bishkek":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(7)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q7()

def q8():
    global totalCorrect
    global loops
    global qsLeft
    global player
    global p1totalCorrect
    global p2totalCorrect
    ans = str(input("Which of these countries has the largest surface area? Argentina, Saudi Arabia, Mexico or India: "))
    if str.lower(ans) == "india":
        if player == True:
            p1totalCorrect = p1totalCorrect + 1
        else:
            p2totalCorrect = p2totalCorrect + 1
        print ("Correct answer! You gained 1 point\n")
        loops = loops + 1
        qsLeft.remove(8)
        player = not player
    elif str.lower(ans)=="argentina" or str.lower(ans)=="saudi arabia" or str.lower(ans)=="mexico":
        print ("Wrong Answer. You were not awarded a point\n")
        loops = loops + 1
        qsLeft.remove(8)
        player = not player
    else:
        print("You did not enter a valid answer\n")
        q8()

def randomq():
    if player == True:
        print ("Player 1:")
    else:
        print ("Player 2:")
    questionNum = random.choice(qsLeft)
    {1: q1,
    2: q2,
    3: q3,
    4: q4,
    5: q5,
    6: q6,
    7: q7,
    8: q8}[questionNum]()

while loops < 6:
    randomq()

print ("Final score:\nPlayer 1: " + str(p1totalCorrect) + " points\nPlayer 2: " + str(p2totalCorrect) + " points")
if (p1totalCorrect > p2totalCorrect):
    print ("\nPlayer 1 wins!")
elif (p2totalCorrect > p1totalCorrect):
    print ("\nPlayer 2 wins!")
else:
    print ("\nIt's a tie!")
