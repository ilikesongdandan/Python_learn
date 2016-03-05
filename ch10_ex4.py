fhand=open("mbox-short.txt")
couts=dict()
for line in fhand:
	if not line.startswith("From"):continue
	words=line.split()
	if len(words)<5:continue
	time=words[5].split(':')
	couts[time[0]]=couts.get(time[0],0)+1
times=list()
ex=couts.items()
print ex

for hour,val in couts.items():
	times.append((hour,val))
times.sort()
for time_ in times:
	print time_[0],time_[1]
