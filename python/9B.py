from tkinter import *
import tkinter as t
m=t.Tk()
m.title("Fill your Details")
def button():
 selectionE="Your Name:",str(va.get())
 selectionCB="\n Hobbies:","Dance",str(cvar1.get()),"Music",str(cvar2.get())
 selectionRB="\n Gender:",str(rvar1.get())
 selectionS="\n Marks:",str(varS.get())
 selection=selectionE+selectionCB+selectionRB+selectionS
 ls=t.Label(m,text=selection).grid()
m1=t.Message(m,text="Fill your Details").grid(row=1,column=0)
l=t.Label(m,text="Enter your name:",relief="ridge").grid(row=2,column=0)
va=StringVar()
el=t.Entry(m,textvariable=va,width=30,relief="raised").grid(row=2,column=1)
l1=t.Label(m,text="Select Your Hobbies:",relief="raised").grid(row=3,column=0)
cvar1=IntVar()
cvar2=IntVar()
c1=Checkbutton(m,text="Dance",variable=cvar1,relief="raised").grid(row=3,column=1)
c2=Checkbutton(m,text="Music",variable=cvar2,relief="raised").grid(row=4,column=1)
l2=t.Label(m,text="Select your Gender:",relief="ridge").grid(row=5,column=0)
rvar1=IntVar()
r1=t.Radiobutton(m,text="Male",variable=rvar1,value=1,relief="raised").grid(row=5,column=1)
r2=t.Radiobutton(m,text="Female",variable=rvar1,value=2,relief="raised").grid(row=6,column=1)
l3=t.Label(m,text="Enter your marks:",relief="ridge").grid(row=7,column=0)
varS=DoubleVar()
sc=t.Scale(m,from_=0,to=150,orient="horizontal",variable=varS,relief="raised").grid(row=7,column=1
)
b1=t.Button(m,text="Submit",command=button).grid(row=8,column=0)
m.mainloop()