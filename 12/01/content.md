#Pseudocode corrections

##TASK 1

```
fruit ← 0
stationary ← 0
vegetables ← 0
other ← 0
drinks ← 0
NumberOfProducts ← 0
WHILE NumberOfProducts <= 9000
  DO
    INPUT code
    IF code < 1000 THEN
      fruit ← fruit + 1
      NumberOfProducts ← NumberOfProducts + 1
    ELSE IF code < 2000 THEN
      stationary ← stationary + 1
      NumberOfProducts ← NumberOfProducts + 1
    ELSE IF code < 3000 THEN
      vegetables ← vegetables + 1
      NumberOfProducts ← NumberOfProducts + 1
    ELSE IF code < 9001 THEN
      other ← other + 1
      NumberOfProducts ← NumberOfProducts + 1
    ELSE IF code < 5000 THEN
      drinks ← drinks + 1
      NumberOfProducts ← NumberOfProducts + 1
    ELSE
      PRINT “Code not valid. Please re-enter”
    ENDIF
ENDWHILE
PercentageOfFruits = fruits / NumberOfProducts * 100
PercentageOfStationary = stationary / NumberOfProducts * 100
PercentageOfVegetables = vegetables / NumberOfProducts * 100
PercentageOfDrinks = drinks / NumberOfProducts * 100
PercentageOfOther = other / NumberOfProducts * 100
OUTPUT “Percentage of stationary was “ + PercentageOfStationary
OUTPUT “Percentage of vegetables was “ + PercentageOfVegetables
OUTPUT “Percentage of drinks was “ + PercentageOfDrinks
OUTPUT “Percentage of fruis was “ + PercentageOfFruits
OUTPUT “Percentage of other was “ + PercentageOfOther
```

##Task 2

```
NumberOfResorts ← 0
NumberOfDays ← 0
WHILE NumberOf Resorts DO
  REPEAT
    INPUT Rainfall
    IF Rainfall < LowestRainfall
      THEN
        PRINT “Please enter snowfall”
    ELSE
      PRINT “Please enter snowfall”
    ENDIF
  TotalRainfall ← TotalRainfall + Rainfall    
  AverageRainfall ← TotalRainfall/365
  INPUT Snowfall
  TotalSunshineHours ← TotalSunshineHours + SunshineHours
  IF SunshineHours > HighestSunshineHours
    THEN  
      HighestSunshineHours ← SunshineHours
      PRINT “Thank you for your entry”
  ELSE
    PRINT “Thank you for your entry”
  ENDIF
  AverageSunshineHours ← TotalSunshineHours/365
  OUTPUT AverageSunshineHours
  UNTIL NumberOfDays > 364
  NumberOfResorts ← NumberOfResorts
ENDWHILE
OUTPUT HighestSunshineHours
OUTPUT LowestRainfall
```

##Task 3

```
FOR VehicleCount = 1 to 200
MaximumSpeed ← 100
INPUT Time
OUTPUT TotalSpeeders
OUTPUT Speed
IF Speed > MaximumSpeed THEN
  TotalSpeeders ← TotalSpeeders + 1
  PRINT “Speed exceeds 100km/hour”
  IF Speed > HighestSpeed THEN
    HighestSpeed ← Speed
  ELSE
    Speed ← Distance/Time
    PRINT “Thank you for your entry”
    TotalSpeeders ← 0
  ENDIF
  Distance ← 0.1
ENDIF
NEXT VehicleCount
OUTPUT HighestSpeed
OUTPUT Speed
PercentageSpeeders ← TotalSpeeders/VehicleCount*100
HighestSpeed ← 0
OUTPUT PercentageSpeeders
```
