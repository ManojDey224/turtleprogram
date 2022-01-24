from tkinter import Tk,Label,Y,RIGHT
root=Tk()
label1=Label(root,text="welcome to python!",background='red')
label2=Label(root,text="have a good morning",background='green')
label1.pack(fill=Y,padx=10,ipady=25,side=RIGHT)
label2.pack(fill=Y,padx=20,ipady=40,side=RIGHT)
root.mainloop()