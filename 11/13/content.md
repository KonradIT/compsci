##Pseudocode

Scenario:

System enables users to input 10 numbers only and output the total.

FOR count = 1 TO 10
	INPUT number
	total <- total + number
NEXT count
OUTPUT total

REPEAT UNTIL COUNT = 10
	THEN
		TOTAL <- TOTAL + NUMBER
	COUNT = COUNT + 1
ENDREPEAT

---

COUNT = 1
WHILE COUNT <= 10
	INPUT Number
	TOTAL <- TOTAL + NUMBER
	COUNT <- COUNT + 1
ENDWHILE
OUTPUT Total

Exercise:

COUNT = 1
REPEAT
	INPUT Forename
	INPUT Surname
	OUT “Forename: “ + Forename + “Surname: “ + Surname
UNTIL Count = 15

Count = 1
WHILE Count = 10
	DO
		INPUT Forename
		INPUT Surname
		OUT “Forename: “ + Forename + “Surname: “ + Surname
ENDWHILE

Count = 0
FOR Count = 0 TO 14
	NEXT
		INPUT Forename
		INPUT Surname
		OUT “Forename: “ + Forename + “Surname: “ + Surname
ENDFOR
