'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name + " and I am" , int(self.age) , "years old.")

p1 = Person("John", 36)
p1.myfunc()'''

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade =grade

    def intro(self):
        print(f"Name: {self.name} \nGrade: {self.grade}th grade.")
    
s1 = Student("Amy",9)
s1.intro()
        