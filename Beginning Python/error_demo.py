try:
	print 'try...'
	r=10/0
	print ('result',r)
# except Exception, e:
except ZeroDivisionError,e:
	# raise 'error',e
	print 'exceptr',e
	# raise ValueError('input error')
# else:
	# pass
finally:
	# pass
	print 'finally....'
print 'END'