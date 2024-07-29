import tkinter as tk
from tkinter import*


root=tk.Tk()

root.title("First Tkinter Experience")

root.geometry("500x500")

label=tk.Label(root,text="Tkinter",font=("Ariel",18))
label.pack(padx=20,pady=20)

text=tk.Text(root,height=3,font=("Ariel",9))
text.pack(padx=20)

entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="SUBMIT",font=("Ariel",12))
button.pack(pady=10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

button1=tk.Button(buttonframe,text='1',font=("Ariel",18))
button1.grid(row=0,column=0,sticky=tk.W+tk.E)

button2=tk.Button(buttonframe,text='2',font=("Ariel",18))
button2.grid(row=0,column=1,sticky=tk.W+tk.E)

button3=tk.Button(buttonframe,text='3',font=("Ariel",18))
button3.grid(row=0,column=2,sticky=tk.W+tk.E)

button4=tk.Button(buttonframe,text='4',font=("Ariel",18))
button4.grid(row=1,column=0,sticky=tk.W+tk.E)

button5=tk.Button(buttonframe,text='5',font=("Ariel",18))
button5.grid(row=1,column=1,sticky=tk.W+tk.E)

button6=tk.Button(buttonframe,text='6',font=("Ariel",18))
button6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

anotherbtn=tk.Button(root,text="TEST")
anotherbtn.place(x=200,y=200,height=100,width=100)

root.mainloop()
