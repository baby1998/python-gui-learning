from Tkinter import *
from Tkinter import Combobox

def page():
	etxt=mint.get()
	etxt2=mint2.get()
	l=Label(win,text=etxt).pack(side="left")
	l2=Label(win,text=etxt2).pack(side="left")
	return

win=Tk()
win.geometry("500x500")
		
mint=StringVar()
mint2=StringVar()

	
la=Label(win,text="Welcome In My First GUI Programme !",bg="yellowgreen",width=50,height=7,font=45).pack()		
line=Label(win,text="----------------------------------------------------------------").pack()
label=Label(win,text="Username:",fg="blue",font=30).pack()
input1=Entry(win,textvariable=mint,bg="tomato",width=30).pack()
line2=Label(win,text="     ").pack()
label2=Label(win,text="Password:",fg="blue",font=30).pack()
input2=Entry(win,textvariable=mint2,bg="tomato",width=30,show="*").pack()
line3=Label(win,text="     ").pack()
btn=Button(win,text="REGISTER IT !",bg="deeppink",command=page).pack()
win.mainloop()

if __name__=='__main__':
	page()



