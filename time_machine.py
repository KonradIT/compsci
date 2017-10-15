import time
import subprocess
import random

class TimeMachine:
  def __init__(self):
    self.items=[["Petri Dish","Fleming"," ","1887"],["Cathode Tube","Wilhem Roentgen"," ","1904"],["Rock with ingition properties","First humans"," ","2M BC"]]
    self.GameLost = False
    self.Points = 0
    self.Definitions = [
      ["What is\"2+2-1\"?","3"],
      ["When did Donald Trump win the Presidential Race?","2016"],
      ["What is 9 + 10?","19"],
      ["What is the square root of 49?","7"],
      ["Who was the first man to step on the moon?","neil armstrong"],
      ["Who turned all he touched to gold?","Midas"],
      ["What is the capital of Greece?","Athens"],
      ["Parma and Tuscany are regions of what country?","Italy"],
      ["What US state includes the telephone area code 501?","Arkansas"],
      ["What city is home to The CN Tower?","Toronto"],
      ["What is the capital of Bulgaria?","Sofia"],
      ["In what country is the holy city of Mecca?","Saudi Arabia"]

    ]
    self.ChosenAnswers=[]
    self.Choice=""
  def flux_capacitor(self):
    empty=0    
    for i in self.items:
        if i[2] == " ":
            empty += 1
    if empty != 0:
        print("\t\t>>> Delive these items: ")
        count=0
        for index, i in enumerate(self.items):
            if i[2] == " ":
                count += 1
                if count != 0:
                    print("\t\t " + str(index+1) + " - [" + i[2] + "] " + i[3] + " - " + i[0] + " to " + i[1])
    else:
        print("\t\t>>> All questions answered.\n\t\t>>> You won.")
        exit()
    choice=input("\t\t>>> Enter: ")
    self.answer(choice)
  def answer(self, choice, Attempts=4, Answer=""):
    i=random.randint(0,10)
    self.Choice=choice
    if Answer != "":
        attempts=Attempts
        ans=Answer
        if attempts == 0:
            print("\t\t!!! The artifact thief escaped. Try again next time.")
        else:
            print("\n\t\t"+ans)
            print("\t\t>>> Attempts: " + str(attempts))
            answer=input("\t\t>>> Answer: ").lower()
            if answer == self.Definitions[i][1].lower():
                self.items[int(choice)-1][2] = "X"
                self.ChosenAnswers.append(self.Definitions[i][0])
            else:
                attempts -= 1
                self.answer(self.Choice, attempts, ans)
    elif self.Definitions[i][0] not in self.ChosenAnswers:
        attempts=Attempts
        if attempts == 0:
                print("The artifact thief escaped. Try again next time.")
        else:
            ans = self.Definitions[i][0]
            print("\n\t\t" + self.Definitions[i][0])
            print("\t\t>>>Attempts: " + str(attempts))
            answer=input("\t\t>>> Answer: ").lower()
            if answer == self.Definitions[i][1].lower():
                self.items[int(choice)-1][2] = "X"
                self.ChosenAnswers.append(self.Definitions[i][0])
            else:
                attempts -= 1
                self.answer(self.Choice, attempts, ans)
  def item_status(self,item,status="None"):
    if item <= len(self.items):
      if status == "None":
        return self.items[item][0]
      else:
        self.items[item][2] = status

if __name__ == "__main__":
    delorean = TimeMachine()
    while delorean.GameLost == False:
      delorean.flux_capacitor()



