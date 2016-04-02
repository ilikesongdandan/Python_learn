import functools
def log(func):


	if callable(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'before call'+func.__name__
			print '%s()' %(func.__name__)
			print 'after call'+func.__name__
			return func(*args,**kw)
		return wrapper
	else :
		def decorator(func2):
			@functools.wraps(func2)
			def wrapper(*args,**kw):
				print 'before call'+func+func2.__name__
				print '%s()' %(func2.__name__)
				print 'after call'+func+func2.__name__
				return func2(*args,**kw)
			return wrapper
		return decorator
@log
def f1():
	# pass
	print 'doing1'

@log('execute')
def f2():
	# pass
	print "doing2"


f1()
f2()