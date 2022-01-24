import os
import platform

global studentlist
studentlist = ["manoj kumar dey", "rahul pal","anik sarkar","shew narayan ray","jeet bhattacharya"]

def studentmanagement():

print("\n++ welocome to serampore collage student management list ++\n")
print("[choice 1: showing the list of the student]")
print("[choice 2: add new student]")
print("[choice 3: searching student]")
print("[choice 4: deleteing a student]")

try:
x=int(input("enter the choice:"))
except ValueError:
exit("\nHy! this is not a number")
else:
print("\n")

 if(x==1):
print("Student List\n")
for students in studentlist:
print("++{}++".format(students))

elif(x==2):
    studentnew =input("enter the student")
if(studentnew in studentlist):
print("\n this student {} Already in the table".format(studentnew))
else:
        studentlist.append(studentnew)
print("\n++ new student {} Added sucessfully ++\n")
for students in studentlist:
print("++{}++".format(students))

elif(x==3)
    studentsearching= input("choose the student name to search")
if(studentsearching in studentlist):
print("\n++ there is a found of this student {} ++" .format(studentsearching))
else:
print("\n there is a no record found of this students {} ++".format(studentsearching))

elif(x==4):
studentdelete=input("choose the student name to delete")
if(studentdelete in studentlist):
studentlist.remove(studentdelete)
for students in studentlist:
print("++{} ++".format(students))
else:
print("\n++ there is no record fiund of this students {} ++".format(studentdelete))

elif(x &lt; 1 or x &gt; 4):
print("enter the valid chose")

studentmanagement()

def continueAgain()
runningagain=input("\n want to continue this process yes/no: ")
if(runningagain.lower() == 'yes'):
if(platform.system() =="windows"):
print(os.system('cls'))
else:
print(os.system("clear"))
studentmanagement()
continueAgain()
else:
quit()

continueAgain()