class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Teacher(Person):
    def _init_(self, name, age,exp,r_area):
        Person._init_(self, name, age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("EXPERINCE:",self.exp)
        print("RESEARCH AREA:",self.r_area)
class Student(Person):
    def _init_(self, name, age,course,marks):
        Person._init_(self, name, age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("COURSE:",self.course)
        print("MARKS:",self.marks)
        print("***********TEACHER***********")
        T=Teacher("SHIBDAS",43,20,"DATA SCIENCE")
        T.displayData()
        print("************STUDENT***********")
        S=Student("MANOJ",34,"BTECH",78)
        S.displayData()