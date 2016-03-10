import urllib
from bs4 import BeautifulSoup
url=raw_input("Enter a url:")
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")

#Retrieve all of the anchor tages
tags=soup('a')
for tag in tags:
	#look at the parts of a tag
	print 'Tag:',tag
	print 'URL:',tag.get('href',None)
	print 'Content',tag.contents
	print 'Attrs',tag.attrs