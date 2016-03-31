import math

def is_sushu(n):
	
	if n==1:
		return False
	else :
		# y=int(math.sqrt(n))
		a=range(1,n+1)
		count=0
		for i in a:
			if n%i==0:
				count=count+1

		if count>2:
			return True
		else :
			return False

l=filter(is_sushu, range(1,101))
print l
