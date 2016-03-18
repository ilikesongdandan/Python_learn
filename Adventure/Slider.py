import Tkinter as tk
window=tk.Tk()


def changeSlider(number):
	num=slider.get()
	num=str(num)
	entery.delete(0,tk.END)
	entery.insert(0, num)
	# pass
slider=tk.Scale(window,from_=0,to=100,command=changeSlider)
label=tk.Label(window,text="Num")
entery=tk.Entry(window)

slider.pack()
label.pack()
entery.pack()
window.mainloop()