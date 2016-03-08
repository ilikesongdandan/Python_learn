import re
fhand=open('regex_sum_247511.txt')
num=0
for line in fhand:
	line=line.rstrip()
	x=re.findall('[0-9]+',line)
	len_=len(x)
	for i in range(len_):
		num_=int(x[i])
		num=num+num_
# num=int(num)
print num

print sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_247511.txt').read())])
