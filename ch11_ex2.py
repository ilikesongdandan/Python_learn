import re
l='My 2 favorite numbers are 19 and 42'
m='abbb'

x=re.findall('^ab*?',m)
x_=re.findall('^a.*?',m)
x__=re.findall('^a.',m)
x___=re.findall('^a\S',m)
x_1=re.findall('^a\S+',m)
y=re.findall('^ab+?',m)
z=re.findall('[1-9]+',l)
lst=l.split()
print type(lst[1])

num='00.123456'
num_=re.findall('[0-9.]+',num)
print num_

print x,x_,x__,x_1,y,z

# hand=open('mbox-short.txt')
# for line in hand:
	# line=line.rstrip()
	# if re.search('^X-.+: [0-9.]',line):
		# print line
hand=open('mbox-short.txt')
for line in hand:
	line=line.rstrip()
	x=re.findall('^X\S*: ([0-9.]+)',line)
	# print x
	if len(x)>0:
		print x