count=0
total=0
average=0
while True:
	inp=raw_input("Enter a number:")
	if inp=='done':
		break
	else:
		try:
			inp=float(inp)
			#count=count+1
			#total=total+inp
		except:
			print "Please enter a number"
			continue
		inp=float(inp)
		count=count+1
		total=total+inp
average=total/count
print count,total,average
