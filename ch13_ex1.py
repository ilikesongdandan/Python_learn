import xml.etree.ElementTree as ET
data = '''
<persons>	
	<person>
		<name>Chuck</name>
		<phone type="intl">
		+1 734 303 4456
		</phone>
		<email hide="yes">123456789@163.com</email>
	</person>
	<person>
		<name>wangjj</name>
		<phone type="intl">
		13052226391
		</phone>
		<email hide="yes">wangjj886688@163.com</email>
	</person>
</persons>'''
tree=ET.fromstring(data)
# l=tree.findall('persons')
# print len(l)
lst=tree.findall('person')
print len(lst)
for item in lst:
	print 'Name:',item.find('name').text
	print 'Atttr:',item.find('email').get('hide')
	print 'email:',item.find('email').text
	print 'phone:',item.find('phone').text
