import re
hand=open('mbox-short.txt')
x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
x_01=re.findall('@[^ ]+',x)
print x_01


for line in hand:
	line=line.rstrip()
	y=re.findall('^From .*(@[^ ]+)',line)
	if len(y)>0:
		print y

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print y

a="a b c define"
b=re.findall('\sb\s\S*',a)
print b


x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
num=re.findall('[0-9]+',x)
print num