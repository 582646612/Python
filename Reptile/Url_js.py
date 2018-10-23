# -*- coding:utf-8 -*-

import urllib
import urllib2
import re


class Spider:

    def __init__(self):
        self.siteURL = 'https://v.taobao.com/v/content/live?catetype=704&from=taonvlang'

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        # 模拟Mozilla浏览器进行爬虫
        request.add_header("user-agent", "Mozilla/5.0")
        response2 = urllib2.urlopen(request)
        return response2.read()

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        print page
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item[0], item[1], item[2], item[3], item[4]


spider = Spider()
spider.getContents(1)