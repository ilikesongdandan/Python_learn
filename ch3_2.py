inp=raw_input('Enter Hours:')
Hours=float(inp)
inp=raw_input('Enter Rate:')
Rate=float(inp)
if Hours>40:
	Pay=40*Rate+(Hours-40)*1.5*Rate
	print "Pay: ",Pay
else :
	Pay=Hours*Rate
	print "Pay: ",Pay

