# -*- coding: UTF-8 -*-

import re

from bs4 import BeautifulSoup
# pip BeautifulSoup4
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
# 获取所有的链接
links = soup.find_all('a')
print ("所有的链接")
for link in links:
    print ()

print ()
link_node = soup.find('a', href="http://example.com/elsie")
print (link_node.name, link_node['href'], link_node['class'], link_node.get_text())

print ("正则表达式匹配")
link_node = soup.find('a', href=re.compile(r"ti"))
print (link_node.name, link_node['href'], link_node['class'], link_node.get_text())

print ("获取P段落的文字")
p_node = soup.find('p', class_='story')
print (p_node.name, p_node['class'], p_node.get_text())


'''
soup.select('a[href]')某个属性来查找
soup.select('a[href^="http://example.com/"]')  #匹配值的开头
soup.select('a[href$="tillie"]')  #匹配值的结尾
soup.select('a[href*=".com/el"]')  #模糊匹配
soup.select('.title')  CSS类名查找
soup.select('[class~=title]')
tag的id查找
soup.select('#link1')
soup.select('a#link2')
'''