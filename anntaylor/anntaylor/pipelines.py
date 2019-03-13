# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
class AnntaylorPipeline(object):
    def process_item(self, item, spider, response):
        if item['originalPrice']:
            originalprice=("".join(item['originalPrice']))
            originalprice=[e for e in re.split("[^0-9]", originalprice) if e != '']
            item['originalPrice'] =max(map(int, originalprice))
            return item
