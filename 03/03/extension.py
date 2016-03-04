studentMark = []
numberOfMarks = 0
count = 0
def calculate():
        print(studentMark,count)
def setNumberOfMarks():
        numberOfMarks = input("Number of marks: ")
def addMark():
  global count
  mark=input("Please enter the mark: ")
  if mark == "done":
          calculate()
  else:
          studentMark.append(mark)
          addMark()
          count = count + 1

if __name__ == '__main__':
    addMark()

