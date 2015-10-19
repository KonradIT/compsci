##Switch case

```

INPUT MonthNumber
CASE MonthNumber OF
1: MonthName <- “January”
    2: MonthName <- “February”
    3: MonthName <- “March”
    4: MonthName <- “April”
    5: MonthName <- “May”
    6: MonthName <- “June”
    7: MonthName <- “July”
    8: MonthName <- “August”
    9: MonthName <- “September”
    10: MonthName <- “October”
    11: MonthName <- “November”
    12: MonthName <- “December”
    OTHERWISE
        OUTSTDIO “Please enter a number between 1 and 12”
        MonthName <- “null”
ENDCASE
OUTSTDIO “The actual Month is “, MonthName

```

---

###Debugging in pseudocode

#####Original:

```
Large = 987
Counter = 0
WHILE Counter > 25
DO
    INPUT Number
    IF Number < Large THEN Large = Number
    Counter = Counter - 2
    ENDWHILE
PRINT Large
```

#####Debugged:

```
Large = 0
Counter = 0
WHILE Counter < 5
    DO
        INPUT Number
        IF Number > Large
            THEN
                Large = Number
                Counter = Counter + 1
        ENDIF
ENDWHILE
PRINT Large
```

###Tips for debugging pseudocode

* Variables, like Total, misplaced or missing
* Incorrect values assigned to variables
* Incrementation and decrementation mixed up
* Pseudocodes in wrong places
* Pseudocodes missing
* Incorrect use of operators such as + and -

---

###What is this for?

It asks a user to enter their favorite subject, and until its not computer science it loops.

