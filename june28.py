from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox

def cmd1():
    lb1.configure(text="acadview")


def cmd2():
    a=askopenfile()

root= Tk ()
root.geometry("500x500")
menu= Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='new',command=cmd1)
filemenu.add_command(label='open',command=cmd2)
filemenu.add_separator()
filemenu.add_command(label='exit',command=root.quit)
lb1=Label(root,text="hello")
lb1.pack()



from tkinter import *
main=Tk()
ourMessage="this is ourmessage"
messageVar=Message(main,text=ourMessage)
messageVar.config(bg='grey')
messageVar.pack()

from tkinter import *

from tkinter.filedialog import askopenfile
from tkinter import messagebox
master=Tk()
def cmd1():
    lb1.configure(text="acadview")


def cmd2():
    a=askopenfile()

def calculate():
    a=w1.get()
    b=w2.get()
    messagebox.showerror(('info',str(a)+""+str(b)))

menu= Menu(master)
master.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='new',command=cmd1)
filemenu.add_command(label='open',command=cmd2)
filemenu.add_command(label='calculate',command=calculate)
master=Tk()
w1=Scale(master,from_=0,to=42)
w1.pack()
w2=Scale(master,from_=0,to=200,orient=HORIZONTAL)
w2.pack()
lb=Label(master,text="hello")
lb.pack()
mainloop()
