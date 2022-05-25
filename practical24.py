class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    pass

fname = input("Enter First Name::: ")
lname = input("Enter First Name::: ")
y = Student(fname,lname)
y.printname()
