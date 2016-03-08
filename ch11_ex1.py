import re
hand=open('mbox-short.txt')
for line in hand:
	line=line.rstrip()
	if re.search('From:',line):
		print line
	if re.search('^From:',line):
		print line
	if re.search('^F..m:',line):
		print line

s='Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst=re.findall('\S+@\S+',s)
print lst

fhand=open('mbox-short.txt')
for line in fhand:
	line=line.rstrip()
	x=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
	if len(x)>0:
		print x