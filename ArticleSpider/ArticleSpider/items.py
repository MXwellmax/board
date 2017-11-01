# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    t = scrapy.Field()
    click_num = scrapy.Field()