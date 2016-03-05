fname=raw_input('Enter the file name:')
fhand=open(fname)
count=0
for line in fhand:
	if line.startswith('Subject:'):
		count=count+1
print 'There',count,'Subject lines in',fname