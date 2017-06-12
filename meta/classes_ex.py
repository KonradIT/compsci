from school import Student
from school import School
st = Student(["Art","ICT"], ["Lorem","Ipsum"],"01/01/1970","John Doe",True)
print(str(st))
st.setName("hello")
print(str(st))
st.getName()

sc = School(15,10)
sc.logTeachers("teacher 1")
sc.getTeachers()
