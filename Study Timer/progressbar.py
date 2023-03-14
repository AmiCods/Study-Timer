import tkinter as tik
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time 
from Doit import *
from time_stop import *


root = Tk()
root.geometry("400x600")
root.title("progress")
root.config(bg="#000")
root.resizable(False,False)



s = Style()
s.theme_use("default")
s.configure("TProgressbar", thickness=20,background="red",bd=0)

x=tik.StringVar()
progress = Progressbar(root,style="TProgressbar", length=200, mode='determinate',maximum=100,variable=x)
progress.place(x=100,y=100)

def bar():

    progress.start()

    if progress['value']==100:

        progress.stop()


button_pro = tik.Button(root,text="Start",bg="#ea3548",fg="#fff",bd=0,width=10,height=2,font=("arial 10 bold"),command=bar).place(x=150,y=540)


#button_pro = tik.Button(root,text="stop",bg="#ea3548",fg="#fff",bd=0,width=10,height=2,font=("arial 10 bold"),command=progress.stop).place(x=300,y=540)

def my_disp(*args):
    label1.config(text=x.get())


label1=tik.Label(root,text="00%",font=("arial",8),bg="#000",fg="#fff")
label1.place(x=160,y=120)
x.trace('w',my_disp)


mainloop()