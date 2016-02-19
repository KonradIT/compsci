##Correct the errors

"Lowest" should be 999, count should be 0 instead of 1 to set 0 to 99 which gives 100 numbers, count=count+1 is useless (get rid of it)

###Exerise in pseudocode
```
sum=0
largestNumber=0
number2=0
avg=0
FOR count = 10
  INPUT number
  //needs WIP
  number2=number
  sum=sum+number
  if number2 > LargestNumber
    largestNumber=number2
NEXT count
avg=sum/10
PRINT "The average is: ",avg,"And the largest is: ",largest

```

**Python**

```
sum=0
count=0
largestNumber=0
number2=0
avg=0
for count in range(0, 9):
  number=input("ENTER NUMBER: ")
  //needs WIP
  number2=number
  sum=sum+number
  if (number2 > LargestNumber):
    largestNumber=number2
avg=sum/10
print("The average is: ",avg,"And the largest is: ",largest)

```
