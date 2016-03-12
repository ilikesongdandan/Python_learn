import urllib
from bs4 import BeautifulSoup
url=raw_input("Enter a url:")
# html=urllib.urlopen(url).read()
# soup=BeautifulSoup(html,"html.parser")
# tags=soup('a')

def retrieve(position_=0,url_=str):
	position=0
	html=urllib.urlopen(url_).read()
	soup=BeautifulSoup(html,"html.parser")
	tags=soup('a')
	# retrive=list()
	for tag in tags:
		retrieving=tag.get('href',None)
		position=position+1
		if position==position_:
			return retrieving
			# html_=urllib.urlopen(retrieving).read()
			# print html
			# break

	
count=raw_input("Enter count:")
count=int(count)
position=raw_input("Enter position:")
position=int(position)

print url
for i in range(count):
	url=retrieve(position,url)
	print url