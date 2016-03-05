inp=raw_input('Enter Hours:')

try:
	Hours=float(inp)
except:
	print "Error,please enter numeric input"
	exit()

inp=raw_input('Enter Rate:')
try:
	Rate=float(inp)
except:
	print "Error,please enter numeric input"