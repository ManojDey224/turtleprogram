import random
import tkinter
stats = []
def get_winner(call):
    if random.random()<=(1/3):
        throw ="rock"
    elif(1/3)<random.random()<=(2/3):
     throw ="scissors"
    else:
        throw ="paper"
    if(throw=="rock"and call == "paper")or(throw =="paper"and call=="scissors")\
        or(throw=="scissors"and call=="rock"):
            stats.append('w')
            result="you won!"
    elif throw == call:
        stats.append('D')
        result = "it is a draw"
    else:
        stats.append('l')
        result="you lose"
        global output
        output.config(text="computer did:"+throw +"\n"+result) 
        def pass_s():
             get_winner("scissors")
        def  pass_r():
            get_winner("rock")
            def pass_p():
                get_winner("paper")
        window =tkinter.Tk()
        scissors=tkinter.Button(window,text="scissors",bg="#ff9999",padx=10,pady=5,commad=pass_s,width=20)
        rock=tkinter.Button(window, text="Rock",bg="#80ff80",padx=10,pady=5,commad=pass_r,width=20)
        paper=tkinter.Button(window,text="what's your call",fg="red")
        scissors.pack(side="left")
        rock.pack(side="left")
        paper.pack(side="left")
        output.pack(side="right")
        window.mainloop()
        for i in stats:
            print(i,end="")
        if stats.count('l')>stats.count('w'):
            result="\n you loose the series."
        elif stats.count('l')==stats.count('w'):
            result="\n series ended in a draw"
        else:
            result="\n you win the series"
            
            print(result)