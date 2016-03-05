score=raw_input("Enter Score:")
try:
	score=float(score)
except:
	print "Please input a number"
	quit()
if score<0:
	print "Please input a correct score"
	quit()
elif score<0.6:
	print "F"
elif score<0.7:
	print "D"
elif score<0.8:
	print "C"
elif score<0.9:
	print "B"
elif score<=1:
	print "A"
else :
	print "Please input a correct score"
	quit() 