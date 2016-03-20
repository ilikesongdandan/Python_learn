import json
import urllib

url=raw_input("Enter location:")
print "Retrieving",url
js=urllib.urlopen(url).read()
print "Retrieved",len(js),"characters"
data=json.loads(js)
# print data['comments']
print 'Count:',len(data['comments'])

datas=dict()
datas=data['comments']
# print datas
sum_=0
for item in datas:
	sum_=sum_+item['count']
print 'Sum:',sum_

# print sum(item['count'] for item in datas)

