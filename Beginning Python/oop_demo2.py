class Animal(object):
	def __init__(self):
		super(Animal, self).__init__()

	def run(self):
		print 'Animal is running'


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()
		# self.arg = arg
	def eat(self):
		print 'dog is eating'
	def run(self):
		print 'dog is running'


if __name__=='__main__':
	animal=Animal()
	animal.run()
	dog=Dog()
	dog.run()
	# print (type(animal))

