fhand=open('romeo.txt')
words=[]
for line in fhand:
	word=line.split()
	#if word in words:continue
	length=len(word)
	print length
	for i in range(length):
		if word[i] in words:
			continue
		else :
			words.append(word[i])
	
words.sort()
print words
