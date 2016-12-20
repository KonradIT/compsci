ATHCOUNT=0
FRCOUNT=0
MAXSPEED=0
seconds=0
runnerList=[]
print("Welcome to the speed logger")
while ATHCOUNT != 50:
  ATHCOUNT=ATHCOUNT+1
  seconds = int(input("Enter time taken in seconds for athlete " + str(ATHCOUNT) + ": "))
  forename=input("Enter forename: ")
  surname=input("Enter surname: ")
  speed = 100/float(seconds)
  runnerList.append(str(forename) + " " + str(speed))
  if speed > MAXSPEED:
    MAXSPEED=speed
  if speed >= 10:
    print("Athlete " + str(ATHCOUNT) + " is a fast runner, speed: " + str(speed))
    FRCOUNT=FRCOUNT+1
  else:
    print("Athlete " + str(ATHCOUNT) + " speed: " + str(speed))
pnFR = ((50- float(FRCOUNT))/50)*100
print("Results:\nFast runners: " + str(FRCOUNT) + "\nMax Speed: " + str(MAXSPEED) + "\n Percentage of runners that are not fast runners: " + str(pnFR))
print(runnerList)
