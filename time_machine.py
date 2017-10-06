import time
import subprocess

class TimeMachine:
  def __init__(self):
    self.__items=[["Petri Dish","Fleming"," "],["Cathode Tube","Wilhem Roentgen"," "],["Rock with ingition properties","First humans"," "]]
    self.__GameLost = False
    self.__Points = 0
    self.__Definitions = [
      ["\n\tWhat is\"2+2-1\"?","3"],
      ["\n\tWhen did Donald Trump win the Presidential Race?","2016"],
      ["\n\tWhat is 9 + 10?","19"],
      ["\n\tWhat is the square root of 49","7"]
    ]
    self.print_startmenu()
  def flux_capacitor(self):
    print("\t\t>>> Delive these items: ")
    for i in self.__items:
      print("\t\t [" + i[2] + "] " + i[0])
  def item_status(self,item,status="None"):
    if item <= len(self.__items):
      if status == "None":
        return self.__items[item][0]
      else:
        self.__items[item][2] = status
  def deliver_item(self, item):
    print("Deliver item to:")
  def print_startmenu(self):
    time.sleep(0.1)
    print("             __---~~~~--__                      __--~~~~---__")
    time.sleep(0.1)
    print("            `\---~~~~~~~~\\                    //~~~~~~~~---/'  ")
    time.sleep(0.1)
    print("              \/~~~~~~~~~\||                  ||/~~~~~~~~~\/ ")
    time.sleep(0.1)
    print("                          `\\                //'")
    time.sleep(0.1)
    print("                            `\\            //'")
    time.sleep(0.1)
    print("                              ||          ||    ")  
    time.sleep(0.1)
    print("                    ______--~~~~~~~~~~~~~~~~~~--______              ")
    time.sleep(0.1)
    print("               ___ // _-~      TIME MACHINE      ~-_ \\ ___  ")
    time.sleep(0.1)
    print("              `\__)\/~                              ~\/(__/'   ")       
    time.sleep(0.1)
    print("               _--`-___                            ___-'--_      ")  
    time.sleep(0.1)
    print("             /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\      ")  
    time.sleep(0.1)
    print("            /|        `\         ________         /'        |\     ")
    time.sleep(0.1)
    print("           | `\   ______`\_      \------/      _/'______   /' |      ")    
    time.sleep(0.1)
    print("           |   `\_~-_____\ ~-________________-~ /_____-~_/'   |  ")
    time.sleep(0.1)
    print("           `.     ~-__________________________________-~     .'    ")   
    time.sleep(0.1)
    print("            `.      [_______/------|~~|------\_______]      .'")
    time.sleep(0.1)
    print("             `\--___((____)(________\/________)(____))___--/'   ")        
    time.sleep(0.1)
    print("              |>>>>>>||                            ||<<<<<<|")

    print("\t\t>>> W E L C O M E T O T H E T I M E M A C H I N E")
    print("\t\t>>> You have to deliver the lost items to people throughout history. You'll complete tasks as well.")
    print("\t\t>>> Enter START to start the time machine")
    if input("\t\t>>> ").upper() == "START":
      self.flux_capacitor()

delorean = TimeMachine()
while delorean.__GameLost == False:
  delorean.flux_capacitor()
