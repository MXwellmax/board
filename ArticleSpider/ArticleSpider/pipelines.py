# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item
class JsonWithEncondingPipeline(object):
    def __init__(self):
        self.file = codecs.opem('article.json','w',encoding = "utf-8")
    def process_item(self,item ,spider):
