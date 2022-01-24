from tkinter import Tk,Entry,Button,INSERT
root=Tk()
entry=Entry(root)
entry.pack()
def printMsg():
    print(entry.get())
    button=Button(root, text='print.content',command=printMsg)
    button.pack()
    root.mainloop()