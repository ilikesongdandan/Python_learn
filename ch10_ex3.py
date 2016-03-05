fhand=open("mbox-short.txt")
couts=dict()
for line in fhand:
	if not line.startswith("From"):continue
	words=line.split()
	if len(words)<5:continue
	couts[words[1]]=couts.get(words[1],0)+1

user=list()
for key,val in couts.items():
	user.append((val,key))
user.sort(reverse=True)
print user[0]
print user[0][1],user[0][0]