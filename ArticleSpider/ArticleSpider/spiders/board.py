# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
import requests
import codecs
from ArticleSpider.items import ArticleItem

from urllib import parse


class BoardSpider(scrapy.Spider):
    name = 'board'
    allowed_domains = ['www1.szu.edu.cn/board']
    start_urls = ['http://www1.szu.edu.cn/board/']

    def parse(self, response):
        articleItem = ArticleItem()
        urlzz= r'.*id=.*'

        # urls = response.css("")
        # re_str = response.xpath('//a[@href="view.asp?id=350375"]/b/text()').extract()[0]
        # urls = response.xpath('')

        # re_strs= response.css('a[href="view.asp?id=^\d{n}$"] font::text()')
        # 抓取页面所有的链接
        links = response.xpath('//a[contains(@class ,"fontcolor3")]/@href').extract()
        # 删除不符合条件的url
        for i in range(len(links)):
            try:
                if links[i] != re.compile(urlzz):
                    del links[i]
            except:
                continue

        del links[0]
        for i in range(len(links)):
            links[i]=parse.urljoin(response.url,links[i])








        # a = re.get(url)
        # a.encoding='utf-8'
        # print(a.text)

        # with codecs.open('contents.html','wb',encoding='utf-8') as f:
        #     f.write(a.text)
        for url in links:
            req = requests.get(url)

            if req.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(req.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = req.apparent_encoding

                # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                global encode_content
                encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；

            # print(encode_content)

            # 这里可以不用写,只是方便测试
            with open('contents.html', 'w', encoding='utf-8') as f:
                f.write(encode_content)

            with codecs.open('contents.html', 'r', encoding='utf-8') as f:
                text = f.read()

            soup = BeautifulSoup(text, 'lxml')
            # print(soup.prettify())
            title = soup.title.text
            cont = soup.find_all('p')
            click_num = re.findall(r'点击数:(\d+)', text)
            conts = []
            for i in cont:
                conts.append(i.text)
            t = ''.join(conts)



            # # 保存结果
            # with open('b.txt', 'a+', encoding='utf-8') as f:
            #     f.write(url + '\n')
            #     f.write(title + '\n')
            #     f.write(t + '\n')
            #     f.write(str(click_num) + '\n')
            #     f.write('\n')
            #     # print(title,cont,click_num)

            articleItem["url"] = url
            articleItem["title"] = title
            articleItem["t"] = t
            articleItem["click_num"] = str(click_num)

            yield articleItem
