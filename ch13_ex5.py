import urllib
import xml.etree.ElementTree as ET

url=raw_input("Enter location:")
print 'Retrieving',url
xml=urllib.urlopen(url).read()
print 'Retrieved',str(len(xml)),'characters'
data=ET.fromstring(xml)
lst=data.findall('comments/comment')
# lst=data.findall('.//comment') yiyangde
print 'Count:',len(lst)
sum=0
for item in lst:
	num=item.find('count').text
	num=int(num)
	sum=sum+num
print 'Sum:',sum
