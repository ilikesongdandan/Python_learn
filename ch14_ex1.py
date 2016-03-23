class PartyAnimal:
	"""docstring for PartyAnimal"""
	x=0
	name=""
	def __init__(self, nam):
		# super(PartyAnimal, self).__init__()
		self.name=nam
		print self.name,"constructed"
	def party(self):
		self.x=self.x+1
		print self.name,'party count',self.x
		# pass

s=PartyAnimal('Sally')
s.party()
j=PartyAnimal('jim')
j.party()