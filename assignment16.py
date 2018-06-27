#A16_Q1
import tkinter

top=tkinter.Tk()
a=tkinter.Label(top,text='hello world')
a.pack()
def close_top():
    top.destroy()
def write():
    print("hello world")
top.title("nav")
top.geometry("500x500")

btn=tkinter.Button(top,text="exit",command=close_top)


btn.pack()
btn.place(x=50,y=50)
top.mainloop()


#A16_Q2
import tkinter

top=tkinter.Tk()
def close():
    top.destroy()
def write():
    print("hello world")
top.title("nav")
top.geometry("500x500")
btn=tkinter.Button(top,text="exit",command=close)
btn1=tkinter.Button(top,text="click",command=write)

btn.pack()
btn1.pack()
btn1.place(x=90,y=90)
btn.place(x=50,y=50)
top.mainloop()

#A16_Q3
from tkinter import *
test=Tk()
frame=Frame(test)
frame.pack()
lbl=Label(test,text="hello world")
lbl.pack()
def close():
    test.destroy()
button1=Button(frame,text='exit',fg='blue',command=close)
button1.pack()
def change():
    test.configure(bg='blue')
button2=Button(frame,text='change label',fg='red',command=change)
button2.pack()
mainloop()

#A16_Q4


from tkinter import *
master=Tk()
master.geometry("100x100")
Label(master,text='input').grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
mainloop()


