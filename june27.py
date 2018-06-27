#GUI

import tkinter #as tk
from tkinter import *
top=tkinter.Tk()
top.title("isha")
top.geometry("500x500")
btn=tkinter.Button(top,text="click",command="hey()")

btn.pack()
btn.place(x=50,y=50)

def hey():
    a=10
    b=5
    c=a+b
    print(c)

top.mainloop()

#from tkinter import *
#master=Tk()
#master.geometry("500x500")
#w=Canvas(master,width=40,height=60)
#w.pack()
#Canvas_height=20
#Canvas_width=200
#y=int(Canvas_height/2)
#w.create_line(0,y,Canvas_width,y)
#var1=IntVar()
#Checkbutton(master,text='male',variable=var1).grid(row=0,column=1)
#var2=IntVar()
#Checkbutton(master,text='female',variable=var2).grid(row=1)


#Label(master,text='first name').grid(row=0)
#Label(master,text='LAST NAME ').grid(row=1)
#e1=Entry(master)
#e2=Entry(master)
#e1.grid(row=0,column=1)
#e2.grid(row=1,column=1)



#w.mainloop()

#root=Tk()
#frame=Frame(root)
#frame.pack()
#buttonframe=Frame(root)
#buttonframe.pack(side=BOTTOM)
#redbutton=Button(frame,text='red',fg='red')
#redbutton.pack(side=LEFT)
#greenbutton=Button(frame,text='brown',fg='brown')
#reenbutton.pack(side=LEFT)
#root.geometry("500x500")
#root.mainloop()

#from tkinter import *

#top=Tk()
#lb=Listbox(top)
#lb.insert(1,'python')
#lb.insert(2,'java')
#lb.insert(3,'c')
#lb.insert(4,'c+')
#lb.insert(5,'php')
#lb.pack()
#top.geometry("500x500")
#top.mainloop()
