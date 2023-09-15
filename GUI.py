from tkinter import *
from tkinter import ttk
root = tk()
root.geometry("500x700")
root.config(bg="Yellow")
root.title("Translator")
txt1= label(root,text="Translator",font=(" Time New Roman", 40,"Bold"))
txt1.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)


txt2= label(root,text="Input Region",font=(" Time New Roman", 20,"Bold"),fg="Black")
txt2.place(x=100,y=100,height=20,width=300)

in_txt= Text(frame,font=(" Time New Roman", 40,"Bold"), wrap =WORD)
in_txt.place(x=10,y=130,height=150,width=480)

list = (LANGUAGES)

box1= ttk.Combobox(frame, value=list)
box1.place(x=10,y=300,height=40,width=150)
box1.set("english")

button = Botton(frame,text="Translate" , relief=RAISED)
button.place(x=170,y=300,height=40,width=150)


box2= ttk.Combobox(frame, value=list)
box2.place(x=330,y=300,height=40,width=150)
box2.set("english")


txt3= label(root,text="Output Region",font=(" Time New Roman", 20,"Bold"),fg="Black")
txt3.place(x=100,y=360,height=20,width=300)


ot_txt= Text(frame,font=(" Time New Roman", 40,"Bold"), wrap =WORD)
ot_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
