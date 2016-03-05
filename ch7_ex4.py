fname=raw_input('Enter a file name:')
fhand=open(fname)
count=0
for line in fhand:
	line=line.rstrip()
	count=count+1
	if count>5:
		break
	line=line.upper()
	print line