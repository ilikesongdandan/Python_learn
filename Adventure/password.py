import Tkinter as tk
window=tk.Tk()

def checkPassword():
	password="wangjj"
	enteredPassword=passwordEntry.get()
	if password==enteredPassword:
		confirmLabel.config(text="correct!")
	else:
		confirmLabel.config(text="error!")


passwordLabel=tk.Label(window,text="Password:")
passwordEntry=tk.Entry(window,show="*")
button=tk.Button(window,text="Enter",command=checkPassword)
confirmLabel=tk.Label(window)
passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()
window.mainloop()