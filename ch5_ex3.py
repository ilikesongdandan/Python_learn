largest=None
smallest=None
while True:
	num=raw_input("Enter a number:")
	if num=="done":
		break
	else:
		try:
			num=float(num)
			if largest is None:
				largest=num
			elif largest<num:
				largest=num
			if smallest is None:
				smallest=num
			elif smallest>num:
				smallest=num
		except:
			print "Invalid input"
largest=int(largest)
smallest=int(smallest)

print "Maximum is",largest
print "Minimum is",smallest