##Advantages of top-down design

* Each designed module can be shared with other programmers
* Each programmer in a project can work on separate modules in the algorithm that they have expertise in
* It´s easier to write, test and debug a single module rather than a whole system
* Different designers can work on modules individually then bring the sub-problems together at the end

* Validation = An automatic check to make sure data is sensible and possible
* Verification = A check to see if the data entered is correct

* Trace Table: Used to identify the values of variables through the execution of a program
* Dry Run: Paper-based run through an algorithm or a program

| Term         | Definition                                                                                          | Example in py                       |
|--------------|-----------------------------------------------------------------------------------------------------|-------------------------------------|
| Syntax Error | An error that occur because the programmer does not use the correct language structure in a program | if x = 5                            |
| Logic Error  | An error that causes a program to do something unexpected                                           | if y > 5:,print(“y is less than 5”) |


| Test Description                                    | Test Data Type | Test Data | Expected Outcome |
|-----------------------------------------------------|----------------|-----------|------------------|
| Tests if the customer purchases more than 4 tickets | Normal         | 3         | >4               |
| Tests if the customer purchases more than 4 tickets | Extreme        | 4         | >4               |
| Tests if the customer purchases more than 4 tickets | Invalid        | pi        | >4               |

---

##I/O in Pseudocode

* Variable ← READLINE(films.txt, 4)
* newFilm = “The Lost Weekend”.
  WRITELINE(films.txt, 5, newFilm)
* WRITELINE(films, 4, “”)

```
FUNCTION sumOf(int number1, int number2)
  value=number1+number2
	RETURN(value)
ENDFUNCTION

CALL sumOf(2,5)
>out: 7
```

