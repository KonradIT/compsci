import time
import random
import datetime
print("""\
             __---~~~~--__                      __--~~~~---__
            `\---~~~~~~~~\\                    //~~~~~~~~---/'
              \/~~~~~~~~~\||                  ||/~~~~~~~~~\/
                          `\\                //'
                            `\\            //'
                              ||          ||
                    ______--~~~~~~~~~~~~~~~~~~--______
               ___ // _-~                        ~-_ \\ ___
              `\__)\/~          TIME MACHINE        ~\/(__/'
               _--`-___                            ___-'--_
             /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\\
            /|        `\         ________         /'        |\\
           | `\   ______`\_      \------/      _/'______   /' |
           |   `\_~-_____\ ~-________________-~ /_____-~_/'   |
           `.     ~-__________________________________-~     .'
            `.      [_______/------|~~|------\_______]      .'
             `\--___((____)(________\/________)(____))___--/'
              |>>>>>>||                            ||<<<<<<|
""")
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def travel_to(year):
    time.sleep(2)
    while switch(year):
        if case(2016):
            print ("           TRAVELLING TO " + str(year) + "!")

            break
        if case(2018):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        if case(2024):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        if case(2100):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        if case(1492):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        if case(1386):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        if case(2001):
            print ("           TRAVELLING TO " + str(year) + "!")
            break
        print("ERROR ERROR\nFlux capacitor has been disabled due to input failure. Restart.")
        break
CURRENT_YEAR=datetime.datetime.now().year
TRAVEL_YEARS=[2016,2018,2024,2100,1492,1386,2001]
CHOSEN_YEAR=0
LOADING=["="]
print("           Welcome to the Time Machine\n           Current Year: " + str(CURRENT_YEAR))
print("           Choose the year you would like to travel:")
print("           -----------------------------------------")
count=0
for i in TRAVEL_YEARS:
    print("           " + str(count) + " - " + str(TRAVEL_YEARS[count]))
    count += 1
CHOSEN_YEAR=int(input("           Year: "))
travel_to(TRAVEL_YEARS[CHOSEN_YEAR])
