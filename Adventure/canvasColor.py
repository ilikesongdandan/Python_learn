import Tkinter as tk
window=tk.Tk()
color="#FF0000"

def sliderUpdate(source):
	# pass
	red=redSlider.get()
	green=greenSlider.get()
	blue=blueSlider.get()
	color="#%02x%02x%02x" % (red,green,blue)
	# print type(color)
	canvas.config(bg=color)
	hexText.delete(0,tk.END)
	hexText.insert(0,color)


redSlider=tk.Scale(window,from_=0,to=255,command=sliderUpdate)
greenSlider=tk.Scale(window,from_=0,to=255,command=sliderUpdate)
blueSlider=tk.Scale(window,from_=0,to=255,command=sliderUpdate)
canvas=tk.Canvas(window,height=300,width=300)
hexText=tk.Entry(window)

redSlider.grid(row=1,column=1)
greenSlider.grid(row=1,column=2)
blueSlider.grid(row=1,column=3)
canvas.grid(row=2,column=1,columnspan=3)
hexText.grid(row=3,column=1,columnspan=3)


# redSlider.pack()
# greenSlider.pack()
# blueSlider.pack()
# canvas.pack()
# window.mainloop()
tk.mainloop()