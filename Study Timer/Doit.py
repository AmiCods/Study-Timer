import tkinter as tik
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time 

def task():

	root=tik.Tk()
	root.title("Do it")
	root.iconbitmap("clock2.ico")
	root.geometry("400x600")
	root.config(bg="#000")
	root.resizable(False,False)


	heading_label=tik.Label(root,text="Study Task",font=("arial",30),bg="#000",fg="#ea3548")
	heading_label.pack(pady=10)


	#button_a = tik.Button(root,text="<",bg="#000",fg="#fff",bd=0,width=2,height=1,font=("",20)).place(x=15,y=10)


	o_1=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=100)

	#sub1=StringVar()
	#sub1_h= tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15).place(x=80,y=128)
	#sub1_h.insert(0,"Subject : Task")

	sub1_h = tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15)
	sub1_h.insert(0,"Subject : Task")
	sub1_h.place(x=80,y=128)

	def do1():
		o_1=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="green2",bd=0).place(x=30,y=100)
		

	def undo1():
		o_1=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=100)
		
	button_d1 = tik.Button(root,text="Done",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=do1).place(x=300,y=140)

	button_ud1 = tik.Button(root,text="x",bg="#ea3548",fg="#fff",bd=0,width=2,height=1,font=("arial 10 bold"),command=undo1).place(x=370,y=140)




	o_2=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=180)

	sub2_h = tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15)
	sub2_h.insert(0,"Subject : Task")
	sub2_h.place(x=80,y=207)


	def do2():
		o_2=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="green2",bd=0).place(x=30,y=180)

	def undo2():
		o_2=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=180)
		
	button_d2 = tik.Button(root,text="Done",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=do2).place(x=300,y=213)

	button_ud2 = tik.Button(root,text="x",bg="#ea3548",fg="#fff",bd=0,width=2,height=1,font=("arial 10 bold"),command=undo2).place(x=370,y=213)





	o_3=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=252)


	sub3_h = tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15)
	sub3_h.insert(0,"Subject : Task")
	sub3_h.place(x=80,y=280)



	def do3():
		o_3=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="green2",bd=0).place(x=30,y=252)

	def undo3():
		o_3=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=252)
		
	button_d3 = tik.Button(root,text="Done",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=do3).place(x=300,y=287)

	button_ud3 = tik.Button(root,text="x",bg="#ea3548",fg="#fff",bd=0,width=2,height=1,font=("arial 10 bold"),command=undo3).place(x=370,y=287)




	o_4=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=330)

	sub4_h = tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15)
	sub4_h.insert(0,"Subject : Task")
	sub4_h.place(x=80,y=358)



	def do4():
		o_4=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="green2",bd=0).place(x=30,y=330)

	def undo4():
		o_4=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=330)
		
	button_d4 = tik.Button(root,text="Done",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=do4).place(x=300,y=365)

	button_ud4 = tik.Button(root,text="x",bg="#ea3548",fg="#fff",bd=0,width=2,height=1,font=("arial 10 bold"),command=undo4).place(x=370,y=365)



	o_5=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=410)

	sub2_h = tik.Entry(root,font=("calibri",20),bg="#000",foreground="#fff",bd=0,width=15)
	sub2_h.insert(0,"Subject : Task")
	sub2_h.place(x=80,y=437)



	def do5():
		o_5=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="green2",bd=0).place(x=30,y=410)

	def undo5():
		o_5=tik.Label(root,text="o",font=("arial black",40),bg="#000",foreground="orangered",bd=0).place(x=30,y=410)
		
	button_d5 = tik.Button(root,text="Done",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=do5).place(x=300,y=444)

	button_ud5 = tik.Button(root,text="x",bg="#ea3548",fg="#fff",bd=0,width=2,height=1,font=("arial 10 bold"),command=undo5).place(x=370,y=444)


	th_label=tik.Label(root,text='"Success is the sum of small efforts',font=("gabriola",20),bg="#000",foreground="snow",bd=0).place(x=10,y=495)
	th_label=tik.Label(root,text='Repeated day in and day out"',font=("gabriola",20),bg="#000",foreground="snow",bd=0).place(x=140,y=535)




	root.mainloop()



