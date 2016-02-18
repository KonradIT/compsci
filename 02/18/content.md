##Homework - Execise 6:

**6.1**

```
myAnswer=input("Please enter your name: ")
print(myAnswer)
food=input("Please enter your favorite food: ")
print(food)
```

**6.2**

```
age=input("Please enter your age: ")
agePlusTen = int(age) + 10
print("You will be",agePlusTen,"in 10 years")
```

Added int(age), age is not an integer, a requirement to be able to do *math*

**6.3**

```
number=input("Enter number: ")
number2=int(number)*2
print(number2)
```

**6.4**

```
one = "cheese"
two = "onion"
print("My favourite crisps are {0} and {1}. I love them!".format(one,two))
print("{0} and {1} and {0} and {1} and {0} and {1}".format(one,two))
print("{0}{0}{0} and {1}{1}{1}".format(one,two))
print("You guessed it. The best crisps are {1} and … {0}.".format(one,two))
```

**6.5**

* print("The answer is {0:.3f}".format(number))
  * 98.147
* print("The answer is {0:.1f}".format(number))
  * 98.1
* print("The answer is {0:.0f}".format(number))
  * 98

**6.6**

```
bill=input("Enter bill: ")
percentage=input("Enter percentage for tip: ")
out=int(bill)*int(percentage)
out2=out/100
print("tip: ",out2)
print("total: ",int(out2)+int(bill))
```

**6.7**

1. 

```
number=input("number: ")
number=int(number)**2
print(number)
```

2.
```
number=input("number: ")
number=int(number)**3
print(number)
```

3.
```
number=input("side of a square: ")
number=int(number)*4
print(number)
```

4.
```
length=input("length: ")
width=input("width: ")
length=int(length)*2
width=int(width)*2
out=int(length)+int(width)
print(out)
```

5.
```
length=input("length: ")
out=int(length)*2
print(out)
```

6.

```
length=input("length: ")
width=input("width: ")
depth=input("depth: ")
out=int(length)*int(width)*int(depth)
print(out)
```

7.

*As time of writing* 

```
pounds=input("pounds: ")
out=int(pounds)*1.29
print(out)
```
