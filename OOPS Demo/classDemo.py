class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getMarks(self):
        return self.marks



s1=Student("Sravya",100)
s2=Student("Lakshmi",100)

print(s1.name)
print(s1.marks)
print(s1.getMarks())


print(s2.name)
print(s2.marks)