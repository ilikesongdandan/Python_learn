import re
command=raw_input('Enter a regular expression:')
hand=open('mbox-short.txt')
count=0
for line in hand:
	line=line.rstrip()
	if re.search(command,line):
		count=count+1
print count