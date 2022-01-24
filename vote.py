import datetime
class Person():
    def _init_(self,name,dob):
        self.name =name
        self.dob =dob
        def check(self):
            today = datetime.date.today()
            age =today.year- self.dob.year
            if today< datetime.date(today.year, self.dob.month, self.dob.day):
                age-=1
                if age>= 18:
                    print(self.name,",Congratulation.... You are eligible to vote.")
                else:
                    print(self.name,"Sorry....... You should be at least 18 years of age to cast your vote:")
                    P = Person("MANOJ",datetime.date(1998, 12, 22))
                    P.check()