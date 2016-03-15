import xml.etree.ElementTree as ET
input_='''
<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>000</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''
stuff=ET.fromstring(input_)
lst=stuff.findall('users/user')
print 'User count:',len(lst)
for item in lst:
	print 'Name:',item.find('name').text
	print 'id:',item.find('id').text
	print 'attribute:',item.get('x')