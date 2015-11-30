##How to fix pseudocode and passing an exam in the process

####What is wrong with this pseudocode?

* Stationary = 1000 to 1999
  * to should be either … or a while loop which generates a var for every number.
* IF Code >= 0 && Code < 1000
  * && is used in High level languages eg C++

####Whats wrong with psuedocode (2)?

* >200 should be > 200
* REPEAT, UNTIL, IF, THEN, ELSE, ENDIF!! All these should be in CAPS

```text
VehiclesExceed = 0
UNTIL Count > 200
REPEAT
    INPUT Time
    Speed = 0.1/Time
    IF Speed > 100
        THEN
            VehiclesExceed = VehiclesExceed + 1
            OUTPUT “Speed: “ + Speed + “is above the limit”
        ELSE
            OUTPUT “Speed: “ + Speed + “is OK”
    ENDIF
ENDREPEAT

```
