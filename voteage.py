age= int(input("enter the age :"))
if(age>=18):
    print("you are eligiable")
else:
    yrs=18-age
    print("you have to wait for another"+str(yrs)+"years to cast your vote")