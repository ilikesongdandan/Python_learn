import re
l='My 2 favorite numbers are 19 and 42'
m='abbb'
x=re.findall('^ab*?',m)
x_=re.findall('^a.*?',m)
x__=re.findall('^a.',m)
y=re.findall('^ab+?',m)
z=re.findall('[1-9]+',l)
lst=l.split()
print type(lst[1])


print x,x_,y,z