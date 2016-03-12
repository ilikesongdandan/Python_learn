#-*- coding:utf-8 -*- 
from bs4 import BeautifulSoup
import urllib
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,"html.parser")
print soup.prettify()
print soup.title
print soup.head
print soup.a
# soup.tag 只获取第一个符合要求的标签
# tags=soup('a')
# print tags

print soup.name
print soup.head.name

print soup.p
print soup.p.attrs
print soup.p['class']