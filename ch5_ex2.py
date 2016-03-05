Smallest_so_far=None
print "Before"
things=[1,2,3,4,5,9,11,22,44,23,41]
for thing in things:
	if Smallest_so_far is None:
		Smallest_so_far=thing
	elif Smallest_so_far>thing:
		Smallest_so_far=thing
	print Smallest_so_far,thing
print "After"