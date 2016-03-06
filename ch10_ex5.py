#c={'a':10,'b':1,'c':22}
#print sorted([(v,k) for k,v in c.items()],reverse=True)
fhand=open("mbox-short.txt")
couts=dict()
for line in fhand:
	if not line.startswith("From"):continue
	words=line.split()
	if len(words)<5:continue
	time=words[5].split(':')
	couts[time[0]]=couts.get(time[0],0)+1
times=list()
print couts
ex=couts.items()
print ex

print type(couts.items())
print couts[time[0]]
print type(couts[time[0]])
#for hour,val in couts.items():
#	times.append((hour,val))
#times.sort()
#for time_ in times:
#	print time_[0],time_[1]
times=sorted([(v,h) for v,h in couts.items()])
print times
print type(times[0][0])


for time_ in times:
	print time_[0],time_[1]
