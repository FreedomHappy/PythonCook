import tkinter as tk

window=tk.Tk()
window.title("TK-window")
window.geometry('500x200')

var=tk.StringVar()

l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()

on_hit=False

def hit_you():
	global on_hit
	if on_hit==False:
		on_hit=True
		var.set("OMG!Don't hit me!")
	else:
		on_hit=False
		var.set("")
b=tk.Button(window,text='hit you!',width=15,height=2,command=hit_you)
b.pack()

window.mainloop()