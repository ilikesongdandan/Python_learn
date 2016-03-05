fhand=open('mbox.txt')
count=0
for line in fhand:
	count=count+1
print fhand
print "count:",count

fhand_2=open('mbox-short.txt')
inp=fhand_2.read()
print len(inp)
print inp[:20]

fhand_3=open('mbox-short.txt')
for line_2 in fhand_3:
	line_2=line_2.rstrip()
	if line_2.startswith('From:'):
		print line_2


fhand_4=open('mbox-short.txt')
for line_3 in fhand_4:
	line_3=line_3.rstrip()
	#Skip 'uninteresting lines'
	if not line_3.startswith('From:'):
		continue
	print line_3

fhand_5=open('mbox-short.txt')
for line_4 in fhand_5:
	line_4=line_4.rstrip()
	if line_4.find('@uct.ac.za')==-1:
		continue
	print line_4