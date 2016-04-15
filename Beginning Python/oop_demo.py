class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.name = name
		self.score=score
	def print_score(self):
		print '%s:%s'%(self.name,self.score)

	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else :
			return 'C'


if __name__=='__main__':
	bart=Student('wangjj',"99")	
	bart.print_score()	
	print (bart.get_grade())