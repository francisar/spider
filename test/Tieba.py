# -*- coding:utf-8 -*-
import urllib2
import re


class QTB:
    def __init__(self,url):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.url = url
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False
    def __http__(self):
        try:
            request = urllib2.Request(self.url,headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度百科失败,错误原因",e.reason
                return None
    def spider(self):
        pageCode=self.__http__()
        #pattern = re.compile('<h3.*?class="core_title_txt.*?title="(.*?)".*?>.*?<div.*?class="louzhubiaoshi.*?j_louzhubiaoshi.*?author="(.*?)">.*?<div.*?class="d_post_content j_d_post_content">(.*?)</div>',re.S)
        pattern = re.compile('<h3.*?class="core_title_txt.*?title="(.*?)".*?>.*?<div.*?class="louzhubiaoshi.*?j_louzhubiaoshi.*?author="(.*?)">.*?<div.*?class="d_post_content.*?j_d_post_content.*?>(.*?)</div>',re.S)
        #pattern = re.compile('<div.*?class="d_post_content.*?j_d_post_content.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,pageCode)
        return items


url="http://tieba.baidu.com/p/3817394362?fr=frs"



t=QTB(url)
items=t.spider()
for item in items:
     print item[0],item[1],item[2]