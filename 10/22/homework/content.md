##Homework for 10/22

**Task: Write an algorithm in pseudocode that asks for four numbers to be entered and then adds these up.

If the user enters zero, the program will request that you enter a number.

It counts the number of times the end user has entered a number.

Once four numbers have been entered, the result should be shown to the user**

---

```
VARIABLE Count
VARIABLE Sum
VARIABLE number1
VARIABLE number2
VARIABLE number3
VARIABLE number4

INPUT > number1
INPUT > number2
INPUT > number3
INPUT > number4

IF number1 = 0
  THEN
    WRITE "Enter a number that is NOT 0 or null\n"
    INPUT number1
  ELSE
    Count = Count+1
ENDIF

IF number2 = 0
  THEN
    WRITE "Enter a number that is NOT 0 or null\n"
    INPUT number2
  ELSE
    Count = Count+1
ENDIF

IF number3 = 0
  THEN
    WRITE "Enter a number that is NOT 0 or null\n"
    INPUT number3
  ELSE 
    Count = Count+1
ENDIF

IF number4 = 0
  THEN
    WRITE "Enter a number that is NOT 0 or null\n"
    INPUT number4
  ELSE 
    Count = Count+1
ENDIF

IF Count = 4
  THEN
    Sum = number1+number2+number3+number4
    WRITE "The count of numbers is: " + Count + "And the sum of all the numbers is: " + Sum
  ELSE
    WRITE "TRY AGAIN"
ENDIF
```

