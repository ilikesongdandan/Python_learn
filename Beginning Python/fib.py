def fib(max):
	n,a,b=0,0,1
	while n<max:
		
		# print b
		yield b

		a,b=b,a+b
		n=n+1
# fib(6)
if __name__=='__main__':
	for n in fib(6):
		print n