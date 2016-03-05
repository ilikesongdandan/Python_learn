largest_so_far=-1
print "Before"
things=[1,2,3,4,5,9,11,22,44,23,41]
for thing in things:
	if largest_so_far<thing:
		largest_so_far=thing
	print largest_so_far,thing
print "After"