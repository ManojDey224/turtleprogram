from tkinter import Tk, Toplevel, Button
root=Tk()
top_level_window = Toplevel()
top_level_window.title("Top Level Window")
def destroy_top_level_window():
    top_level_window.destroy()
closeButton=Button(root,text='close Top level window',command=destroy_top_level_window)
closeButton.pack()
root.mainloop()