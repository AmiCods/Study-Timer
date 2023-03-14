import tkinter as tik
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time 
from Doit import *
from time_stop import *
from plyer import notification


root=tik.Tk()
root.title("Study timer")
root.iconbitmap("clock2.ico")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)


    
heading_label=tik.Label(root,text="Study Timer",font=("arial",30),bg="#000",fg="#ea3548")
heading_label.pack(pady=10)


button_a1 = tik.Button(root,text=">",bg="#000",fg="#fff",bd=0,width=2,height=1,font=("",20),command=task).place(x=350,y=10)


#Timer 
hrs=StringVar()
entery_hrs=tik.Entry(root,textvariable=hrs,width=2,font=("arial",50),bg="#000",fg="#fff",bd=0).place(x=30,y=120)
hrs.set("00")

mint=StringVar()
entery_mint=tik.Entry(root,textvariable=mint,width=2,font=("arial",50),bg="#000",fg="#fff",bd=0).place(x=150,y=120)
mint.set("00")

sec=StringVar()
entery_sec=tik.Entry(root,textvariable=sec,width=2,font=("arial",50),bg="#000",fg="#fff",bd=0).place(x=270,y=120)
sec.set("00")

hrs_label=tik.Label(root,text="hrs",font=("arial",12),bg="#000",fg="#fff").place(x=105,y=160)
mint_label=tik.Label(root,text="min",font=("arial",12),bg="#000",fg="#fff").place(x=225,y=160)
sec_label=tik.Label(root,text="sec",font=("arial",12),bg="#000",fg="#fff").place(x=345,y=160)



def time_set():

    pro_1.stop()
    pro_2.stop()
    pro_3.stop()
    pro_4.stop()


    root=tik.Tk()
    root.title("Time Set")
    root.iconbitmap("clock2.ico")
    root.geometry("250x205")
    root.config(bg="#000")

    entery_hrs1=tik.Entry(root,width=2,font=("arial",40),bg="#000",fg="#fff",bd=0)
    entery_hrs1.insert(0,"00")
    entery_hrs1.place(x=5,y=40)

    entery_mint1=tik.Entry(root,width=2,font=("arial",40),bg="#000",fg="#fff",bd=0)
    entery_mint1.insert(0,"00")
    entery_mint1.place(x=83,y=40)

    entery_sec1=tik.Entry(root,width=2,font=("arial",40),bg="#000",fg="#fff",bd=0)
    entery_sec1.insert(0,"00")
    entery_sec1.place(x=163,y=40)

    hrs_label1=tik.Label(root,text="hrs",font=("arial",12),bg="#000",fg="#fff").place(x=60,y=80)
    mint_label1=tik.Label(root,text="min",font=("arial",12),bg="#000",fg="#fff").place(x=137,y=80)
    sec_label1=tik.Label(root,text="sec",font=("arial",12),bg="#000",fg="#fff").place(x=217,y=80)


    def ok():

        global h
        global m
        global s

        global h1
        global m1
        global s1

        h1=int(entery_hrs1.get())
        m1=int(entery_mint1.get())
        s1=int(entery_sec1.get())


        h=int(hrs.get())
        m=int(mint.get())
        s=int(sec.get())

        h1,h=h,h1
        m1,m=m,m1
        s1,s=s,s1

        
        print (h,m,s)
        root.destroy()

    button = tik.Button(root,text="OK",bg="#ea3548",fg="#fff",bd=0,width=7,height=1,font=("arial 10 bold"),command=ok).place(x=95,y=160)

    
#timer finction :
    

    root.mainloop()


button_set = tik.Button(root,text="set",bg="#000",fg="#fff",bd=0,width=2,height=1,font=("arial",15),command=time_set).place(x=20,y=20)


def bar():

    hrs.set(h)
    mint.set(m)
    sec.set(s)


button_pro = tik.Button(root,text="Ready",bg="#ea3548",fg="#fff",bd=0,width=10,height=2,font=("arial 10 bold"),command=bar).place(x=150,y=540)


def timer():
    
        try:
                # the input provided by the user is
                # stored in here :temp
            temp = int(hrs.get())*3600 + int(mint.get())*60 + int(sec.get())
        except:
            print("Please input the right value")
        while temp >-1:
                 
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
          
                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
            hours=0
            if mins >60:
                 
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                hours, mins = divmod(mins, 60)
                 
                # using format () method to store the value up to
                # two decimal places



            hrs.set("{0:2d}".format(hours))
            mint.set("{0:2d}".format(mins))
            sec.set("{0:2d}".format(secs))
          
                # updating the GUI window after decrementing the
                # temp value every time
            root.update()
            time.sleep(1)

            temp -= 1

            


button_start = tik.Button(root,text="Lets Start",bg="#ea3548",fg="#fff",bd=0,width=10,height=2,font=("arial 10 bold"),command=timer).place(x=15,y=540)

def end():

    pro_1.stop()
    pro_2.stop()
    pro_3.stop()
    pro_4.stop()

    tstop()


button_end = tik.Button(root,text="End it",bg="#ea3548",fg="#fff",bd=0,width=10,height=2,font=("arial 10 bold"),command=end).place(x=300,y=540)


    #ProgressBar
    


s = Style()
s.theme_use("default")
s.configure("TProgressbar", thickness=8,background="red",bd=0)
    
x1=tik.StringVar()
pro_1=ttk.Progressbar(root,style="TProgressbar",orient=HORIZONTAL,length=200,mode='determinate',variable=x1)
pro_1.place(x=95,y=250)

x2=tik.StringVar()
pro_2=ttk.Progressbar(root,style="TProgressbar",orient=HORIZONTAL,length=200,mode='determinate',variable=x2)
pro_2.place(x=95,y=310)

x3=tik.StringVar()
pro_3=ttk.Progressbar(root,style="TProgressbar",orient=HORIZONTAL,length=200,mode='determinate',variable=x3)
pro_3.place(x=95,y=380)

x4=tik.StringVar()
pro_4=ttk.Progressbar(root,style="TProgressbar",orient=HORIZONTAL,length=200,mode='determinate',variable=x4)
pro_4.place(x=95,y=450)


def my_disp(*args):
    label1.config(text=x1.get())
    label2.config(text=x2.get())
    label3.config(text=x3.get())
    label4.config(text=x4.get())

label1=tik.Label(root,text="00%",font=("arial",8),bg="#000",fg="#fff")
label1.place(x=325,y=240)
x1.trace('w',my_disp)

label2=tik.Label(root,text="00%",font=("arial",8),bg="#000",fg="#fff")
label2.place(x=325,y=300)
x2.trace('w',my_disp)

label3=tik.Label(root,text="00%",font=("arial",8),bg="#000",fg="#fff")
label3.place(x=325,y=370)
x3.trace('w',my_disp)

label4=tik.Label(root,text="00%",font=("arial",8),bg="#000",fg="#fff")
label4.place(x=308,y=440)
x4.trace('w',my_disp)

zero_label=tik.Label(root,text="0",font=("arial",18),bg="#000",fg="#fff").place(x=25,y=240)
normal_label=tik.Label(root,text="Normal",font=("arial",15),bg="#000",fg="#fff").place(x=325,y=240)

normal2_label=tik.Label(root,text="Normal",font=("arial",15),bg="#000",fg="#fff").place(x=10,y=300)
Good_label=tik.Label(root,text="Good",font=("arial",15),bg="#000",fg="#fff").place(x=325,y=300)

Good2_label=tik.Label(root,text="Good",font=("arial",15),bg="#000",fg="#fff").place(x=10,y=370)
Great_label=tik.Label(root,text="Great",font=("arial",15),bg="#000",fg="#fff").place(x=325,y=370)

Great2_label=tik.Label(root,text="Great",font=("arial",15),bg="#000",fg="#fff").place(x=10,y=440)
Excellent_label=tik.Label(root,text="Excellent",font=("arial",15),bg="#000",fg="#fff").place(x=308,y=440)


root.mainloop()

