import tkinter as tik
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time 

def tstop():

    root=tik.Tk()
    root.title("Stop")
    root.iconbitmap("clock2.ico")
    root.geometry("250x205")
    root.config(bg="#000")
   #root.resizable(False,False)


    heading_label=tik.Label(root,text="Stop Timer",font=("arial",25),bg="#000",fg="#ea3548")
    heading_label.pack(pady=10)
    
    text_label=tik.Label(root,text="You want to stop timer,",font=("arial",13),bg="#000",fg="#fff")
    text_label.place(x=15,y=70)

    text_label=tik.Label(root,text="So, Your timer is stop",font=("arial",13),bg="#000",fg="#fff")
    text_label.place(x=70,y=100)
    
    def ok():
      root.destroy()

    button = tik.Button(root,text="OK",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=ok).place(x=95,y=160)

     
    

    root.mainloop()

