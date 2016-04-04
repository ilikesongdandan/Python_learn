# print "hello world!"
#-*- coding:utf-8 -*-    
'a test module'

__author__='wangjj'

import sys
def _test():
	args=sys.argv
	if len(args)==1:
		print 'hello world'
	elif len(args)==2:
		print 'hello,%s' %args[1]
	else :
		print 'too many arguments'

def test():
	return _test()


if __name__=='__main__':
	test()