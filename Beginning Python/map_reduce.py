def low(s):
	# str=s[:]
	if len(s)==1:
		return s.upper()
	else :
		str_0=s[0].upper()
		str_1=s[1:].lower()
		return str_0+str_1


def tit(name):
	return name[0].upper()+name[1:].lower()

# s='a'
# a=low(s)
# s1='aBc'
# s1=low(s1)
# print a,s1
l=['adam', 'LISA', 'barT']
L=map(low, l)

L2=map(tit, l)


print L
print L2

def prod(x,y):
	return x*y
l2=[1,2,3,4,5]
L3=reduce(prod, l2)
print L3

