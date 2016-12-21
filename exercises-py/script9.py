n = input("Weekday: ")
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

while switch(n):
    if case("Monday"):
        print("Worst day of the week\n"),
        break
    if case("Tuesday", "Wednesday", "Thursday", "Friday"):
        print("Getting closer to the weekend\n"),
        break
    if case("Saturday", "Sunday"):
        print ("Yay, the weekend is here\n"),
        break
    print("Only single-digit numbers are allowed.")
    break
