##Algorithm

####Code:

```
OUTSTDIO "Welcome to football ticket machine"
INPUT "Enter the number of persons attending" -> numPersons
//numPersons is a variable
OUTSTDIO "OK"
INPUT "What is your budget: " -> budget
//budget is a variable
priceTicket = "12"
//priceTicket is a constant
totalPrice = numPersons * priceTicket
OUTSTDIO "The total price for " + numPersons " people at 12$ a ticket is + totalPrice"
IF totalPrice > budget
  THEN
    OUTSTDIO "Sorry, your budget is " + budget + " and the total price is " + totalPrice"
  ELSE
    OUTSTDIO "OK, good to go. In a momemt you will be prompted to enter your method of payment (visa, bitcoin, paypal, amex)
    Launch PaymentActivity.py
ENDIF
```



