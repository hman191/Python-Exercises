class Student:
    
    def __init__(self, name="Student", age="Student", class_="Student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def getscore(self):
        test1 = int(input("Enter score for test 1:"))
        test2 = int(input("Enter score for test 2:"))
        test3 = int(input("Enter score for test 3:"))
        avgtests = (test1 + test2 + test3)/3
        return avgtests

jeff_jefferson = Student("Jeff", "18", "Year 12")
print(jeff_jefferson.name)
print(jeff_jefferson.getscore())

bob_boberson = Student()
print(bob_boberson.name)
