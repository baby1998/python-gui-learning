from Tkinter import *
win=Tk()
win.geometry("1000x800")
class A():
	def play(self):
		txt=name.get()
		txt2=number.get()
		prnt=Label(win,text=txt2).pack()
		prnt=Label(win,text=txt).pack()
		print("hello")
		return

	def one(play,name,number):
		name=StringVar()
		number=StringVar()
		l=Label(win,text="Welcome In Phonebook Application",font=50,bg="coral",width=100,height=5).pack()
		gape=Label(win,text="            ").pack()
		label=Label(win,text="Username:",font=20,fg="blue").pack()
		gape2=Label(win,text="            ").pack()
		entry1=Entry(win,textvariable=name).pack()
		gape3=Label(win,text="            ").pack()
		label2=Label(win,text="Phone Number:",font=20,fg="blue").pack()
		gape4=Label(win,text="            ").pack()
		entry2=Entry(win,textvariable=number).pack()
		gape5=Label(win,text="            ").pack()
		btn=Button(win,text="SAVE DATA !",command=play).pack()
		win.mainloop()

if __name__=='__main__':
	make_fun=A()
	make_fun.one()
