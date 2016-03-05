fhandle=open('mbox-short.txt')
counts=dict()
for line in fhandle:
	line=line.rstrip()
	if not line.startswith('From'):continue
	words=line.split()
	if len(words)<6:continue
	words_=words[1].split('@')
	counts[words_[1]]=counts.get(words_[1],0)+1
print counts