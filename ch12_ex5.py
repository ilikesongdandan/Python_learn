import urllib
from bs4 import BeautifulSoup
url=raw_input("Enter a url:")
html=urllib.urlopen(url).read()
print html
soup=BeautifulSoup(html,"html.parser")

# print soup.prettify()
print soup.head
#Retrieve all of the anchor tages
tags=soup('a')
# print type('tags')
for tag in tags:
	#look at the parts of a tag
	print 'Tag:',tag
	print 'URL:',tag.get('href',None)
	print 'Content',tag.contents
	print 'Attrs',tag.attrs