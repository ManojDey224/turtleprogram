class Date:
    def _init_(self):
        d=m=y=0
        def get(self):
            self.d=int(input("Enter the day:"))
            self.m=int(input("Enter the month:"))
            self.y=int(input("Enter the year"))
            def _eq_(self,D):
                Flag=False
                if self.d==D.d:
                    if self.m==D.m:
                        if self.y== D.y:
                            Flag=True
                            return Flag
            def _It_(self,D):
                Flag=False
                if self.y<D.y:
                    if self.m<D.m:
                        if self.d<D.d:
                            Flag=True
                            return Flag
                        D1 =Date()
                        D1.get()
                        D2=Date()
                        D2.get()
                        print("D1 ==D2",D1==D2)
                        print("D1<D2",D1<D2)