class Student:
    def __init__(self, subjects, teachers, dob, name, male):
        self._subjects = subjects
        self._teachers = teachers
        self._dob = dob
        self._name = name
        self._male = male
    def __str__(self):
        arr =[]
        arr.append(self._subjects)
        arr.append(self._teachers)
        arr.append(self._dob)
        arr.append(self._name)
        arr.append(self._male)
        return str(arr)
    def setName(self, name):
        self._name = name
    def setDob(self, dob):
        self._dob = dob
    def getName(self):
        print(self._name)
    def getDob(self):
        print(self._dob)
class School:
    def __init__(self, rooms, days_left):
        self._teachers = []
        self._students = []
        self._area=1000
        self._rooms=rooms
        self._days_left=days_left
    def logTeachers(self, teacher):
        self._teachers.append(teacher)
    def logStudents(self, students):
        self._students.append(students)
    def getStudents(self):
        print(self._students)
    def getTeachers(self):
        print(self._teachers)
    def getDaysLeft(self):
        print(self._days_left)
