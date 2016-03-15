#-*- coding:utf-8 -*-    
import Tkinter as tk
window=tk.Tk()
count1=0
count2=0

def buttonClick1():
	# print "Beep!"
	global count1
	count1=count1+1
	button1.config(text=str(count1))

def buttonClick2():
	# print "Beep!"
	global count2
	count2=count2+1
	button2.config(text=str(count2))


# 反向书写
def changeString():
	stringToCopy=entry.get()
	stringToCopy=stringToCopy[::-1]
	# print type(stringToCopy)
	# print type(entry)
	# entry.delete(0,tk.END)
	# entry.insert(tk.END,stringToCopy)
	entry.delete(0,tk.END)
	entry.insert(0,stringToCopy)

button1=tk.Button(window,text="Click me_1!",command=buttonClick1)
button2=tk.Button(window,text="Click me_2!",command=buttonClick2)
entry=tk.Entry(window)
button3=tk.Button(window,text="change",command=changeString)


entry.pack()
button3.pack()
button1.pack()
button2.pack()



window.mainloop()