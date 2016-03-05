def min(values):
	samllest=None
	for value in values:
		if samllest is None or value<samllest:
			samllest=value
	return samllest

it=[2,3,4,8,11]
a=min(it)
print a