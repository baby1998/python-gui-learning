from Tkinter import *

def find():
	print(mint.get())
	label=Label(win,text=mint.get()).pack()
	return
def page():
	l=Label(win,text="hello nest page !").pack()

win=Tk()
mint=StringVar()

label2=Label(win,text="Username").pack()
E=Entry(win,textvariable=mint).pack()
btn2=Button(win,command=page).pack()

win.mainloop()

find()	