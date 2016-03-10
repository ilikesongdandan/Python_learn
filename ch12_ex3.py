import urllib
fhand=urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts=dict()
for line in fhand:
	line=line.strip()
	words=line.split()
	for words in words:
		counts[words]=counts.get(words,0)+1
print counts
