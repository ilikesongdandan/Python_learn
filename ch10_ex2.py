import string
fhand=open("romeo-full.txt")
counts=dict()
for line in fhand:
	line=line.translate(None,string.punctuation)
	line=line.lower()
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1

lst=list()
for key,val in counts.items():
	lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst[:10]:
	print key,val