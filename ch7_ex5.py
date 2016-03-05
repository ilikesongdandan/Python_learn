fname=raw_input('Enter the file name:')
fhand=open(fname)
count=0
total=0
for line in fhand:
	line=line.rstrip()
	if line.startswith('X-DSPAM-Confidence:'):
		count=count+1
		line_num=line[20:26]
		#print line_num
		line_num=float(line_num)
		total=total+line_num
average=total/count
print 'Average spam confidence:',average