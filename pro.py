from Tkinter import *
win=Tk()
win.geometry("800x500")
win.grid()
name=StringVar()
phone=StringVar()
class Main():
	def __init__(self):
		frame=Frame(win).pack()
		frame=Label(win,text="Welcome In Pizza Nukkad Shop !",font=50,bg="coral",width=500,height=4).pack()
		#----------------- label for gap --------------------- :
		gap=Label(win,text="          ").pack(side="left")
		#----------------- label for guest name ---------------- :
		guest=Label(win,text="Guest Name :",font=10).pack()
		#----------------- label for gap -------------------------:
		gap2=Label(win,text="          ").pack()
		#----------------------- entry -------------------------:
		user=Entry(win,width=50,textvariable=name).pack()
		#----------------- label for gap -------------------------:
		gap3=Label(win,text="          ").pack()
		#----------------- label for guest name ---------------- :
		number=Label(win,text="Phone Number :",font=10).pack()
		#----------------- label for gap -------------------------:
		gap4=Label(win,text="          ").pack()
		#------------------ phone entry -------------------------:
		number=Entry(win,width=50,textvariable=phone).pack()
		#----------------- label for gap -------------------------:
		gap3=Label(win,text="          ").pack()
		#------------------ Button push --------------------------:
		push=Button(win,text="Submit",bg="orange",width=30,command=page1).pack()
		win.mainloop()

def page1():
	win2=Tk()
	win2.geometry("300x200")
	txt=name.get()
	txt2=phone.get()
	label=Label(win2,text=txt,fg="red").pack()
	labelgap=Label(win2,text="          ").pack()
	label2=Label(win2,text=txt2,fg="red").pack()
	return

if __name__=='__main__':
	a=Main()