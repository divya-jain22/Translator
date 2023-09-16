from googletrans import Translator , LANGUAGES

def transl(text ="type", src="English",dest="Hindi"):
    text4=text
    src1=src
    dest1=dest
    trans= Translator()
    trans1= trans.translator(text,src=src1,dest=dest1)
    return trans1.text

def data():
    inp =box1.get()
    ot = box2.get()
    t= text2.get(1.0,END)
    textget= transl(text=t,src=inp,dest=ot)
    text3.delete(1.0,END)
    text3.insert(END,textget)

