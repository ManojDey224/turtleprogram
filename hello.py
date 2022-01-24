from gtts import gTTS
import  os
fh= open("hello.txt","r")
helloText= fh.read().replace("\n"," ")
language='en'
output=gTTS(text=helloText,lang=language,slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")