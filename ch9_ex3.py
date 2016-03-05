fhandle=open('mbox-short.txt')
count=dict()
for line in fhandle:
	line=line.rstrip()
	if not line.startswith('From'):continue
	words=line.split()
	if len(words)<6:continue
	count[words[2]]=count.get(words[2],0)+1
print count