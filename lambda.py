

def one():
	l = lambda x,y : x==y
	if l("WORD","WORD"):
		print("YES")

one()

def two():
	nlist=[8,9,10,11]
	print(list(map(lambda x:x*5,nlist)))
two()

def three():
	letters=["a","b","c","d"]
	print(list(filter(lambda x: x == "a" or x == "b", letters)))
three()

def four():
	words=["Donald","Nestor","Trump","Perez","Trump","Trump"]
	print(len(list(filter(lambda y: y == "Trump", words))))

four()

class Human():
  def __init__(self,name):
    self.name = name
    
nestor = Human("Nestor")
print("Hi Im {0.name}".format(nestor))