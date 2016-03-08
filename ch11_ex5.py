import re
fname=raw_input('Enter a file name:')
fhand=open(fname)
num=0
total=0
for line in fhand:
	line=line.rstrip()
	x=re.findall('[0-9]+',line)
	l=len(x)
	total=total+l
	for i in range(l):
		num_=float(x[i])
		num=num+num_
print num/total