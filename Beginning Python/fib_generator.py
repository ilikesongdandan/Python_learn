import fib
def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 3
	print 'step3'
	yield 5
o=odd()
o.next()
# o=odd()
o.next()

for n in fib.fib(10):
	print n

