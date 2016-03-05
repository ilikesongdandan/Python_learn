fname=raw_input("Enter a file name:")
if len(fname)<1:
	fname='mbox-short.txt'
fhand=open(fname)
counts=dict()

for line in fhand:
	line=line.rstrip()
	if line.startswith('From'):
		words=line.split()
		if len(words)<1:
			continue
		print words
		counts[words[1]]=counts.get(words[1],0)+1
bigUser=None
bigCount=None
for word,count in counts.items():
	if bigCount is None or count > bigCount:
		bigUser= word
		bigCount = count
print bigUser, bigCount
