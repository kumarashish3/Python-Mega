from tkinter import *

window = Tk()

def convert():
    gram = float(t_value.get())*1000
    pound = float(t_value.get())*2.20462
    ounce = float(t_value.get())*35.274
    t1.insert(END,gram)
    t2.insert(END,pound)
    t3.insert(END,ounce)

b1 = Button(window,text="Covert",command=convert)
b1.grid(row=0,column=2)

b = Label(window,text="Kg")
b.grid(row=0,column=0)

t_value=StringVar()
t = Entry(window,textvariable=t_value)
t.grid(row=0,column=1)

t1 = Text(window,width=10,height=1)
t1.grid(row=1,column=0)
t2 = Text(window,width=10,height=1)
t2.grid(row=1,column=1)
t3 = Text(window,width=10,height=1)
t3.grid(row=1,column=2)



window.mainloop()
