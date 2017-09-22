def one():
	l = lambda x,y : x==y
	if l(input("word1: "),input("word2: ")):
		print("...MATCH")
	else:
		print("NO MATCH")

print("one()")
one()

def two():
	nlist=[8,9,10,11]
	print(list(map(lambda x:x*5,nlist)))
print("two()")
two()

def three():
	letters=["a","b","c","d"]
	print(list(filter(lambda x: x == "a" or x == "b", letters)))
print("three()")
three()

def four():
	words=["Donald","Nestor","Trump","Perez","Trump","Trump"]
	#Using a lambda
	print(len(list(filter(lambda y: y == "Trump", words))))
	#Using the .count function
	print(words.count("Trump"))
print("four()")
four()

def five():

	class Human():
	  def __init__(self,name, other):
	    self.name = name
	    self.other = other
	  def talk(self,personA,personB):
	    print("Hi {}\nIm {}".format(personA.name.upper(),personB.name.upper()))
	nestor = Human("Nestor","Bloomfield")
	bloomfield = Human("Bloomfield","Nestor")
	nestor.talk(nestor, bloomfield)
	bloomfield.talk(bloomfield, nestor)

print("five()")
five()
