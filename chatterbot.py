from chatterbot import chatBot
from chatterbot.trainers import ListTrainers
from tkinter import Tk
bot=chatBot("My Bot")

Convo={
       "Hello"
       "hi there"
       "what is your name?"
       "My name is bot.i am created by manoj"
       "how are you?"
       "I am doing great these days"
       "thank you"
       "which city you belong?"
       "i am from kalkotta"
 }
trainer=ListTrainers(bot)
trainer.train(Convo)
#answer=bot.get_response()
#print(answer)

print("talk to bot")
while True:
    query=input()
    if query== 'exit':
        break
    answer= bot.get_response(query)
    print("bot:",answer)
    
    main=Tk()
    
    main.geometry("500x650")
    main.title("MY chatbot")
    
    photoL=Label(main,image=)
    photoL.pack(pady=5)
    def ask_from_bot():
        query=textF.get()
        answer_from_bot=bot.get_response(query)
        msgs.insert(END,"you:"+query)
        print(type(answer_from_bot))
        msgs.insert(END,"bot:"+str(answer_from_bot))
        textF.delete(0,END)
    frame=Frame(main)
    sc=Scrolbar(frame)
    msg=Listbox(frame,width=80,height=20)
    sc.pack(side=RIGHT,fill=Y)
    msg.pck(side=LEFT,fill=both,pady=10)
    Frame.pack()
    
    textF=Entry(main.font=(verdena,20))
    textF.pack(fill=X,pady10)
    btn=Button(main,text="Ask from bot",font=("verdana",20)command=ask_from_bot)
    btm.pack()
    main.mainloop()