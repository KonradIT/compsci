##For Loops and Turtles

* Array: `NumberArray = []`
* Function: `def menu():`
* Repetition: `while NumbersInArray < 5:` (A While Loop)
* Totalling: `validOption = False`
* Selection: ` option = int(input("Please enter a number from 1 to 5: "))`

###For Loops in Python

**What does this do?**

```
for letter in 'Python':
   print('Current Letter :', letter)
   ```
   
This executes the code each letter in Python is processed. Output is:

```
Current Letter : p
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n
```

If the string has a space it prints the space too.

###For Loops with Arrays

```
myArray = ["One", "Two", "Three"]
for item in myArray:
   print('Current Letter :', item)
```

It prints every item of the array in a new line. Out:

```
Current Letter : One
Current Letter : Two
Current Letter : Three
```

###Print every letter of a item in an array

```
myArray = ["One", "Two", "Three"]
for item in myArray:
   for letter in item:
   	print('Current Letter :', letter)

```

###Multiplies every item in array by 2:

```
myArray = ["2", "42", "1337"]
for index in range(len(myArray)):
   multiply=eval(myArray[index])*2
   print('Number:', myArray[index], 'multiplied by 2: ',multiply)
```
