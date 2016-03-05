def compute(h,r):
	if h>40:
		pay=(h-40)*r*1.5+40*r
	else:
		pay=h*r
	return pay

hours=raw_input('Enter hours:')
hours=float(hours)
rate=raw_input('Enter rate:')
rate=float(rate)
p=compute(hours,rate)
print p