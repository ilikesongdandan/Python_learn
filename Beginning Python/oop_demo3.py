class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
		# self.arg = arg
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value

	@property
	def age(self):
	    return 2016-self._birth


if __name__=='__main__':
	s=Student()
	s.birth=60
	print s.birth
	# s.age=55
	print s.age

	
		