# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
class AnntaylorPipeline(object):
    def process_item(self, item, spider):
        if item["currentPrice"]:
            currentPrice = ("".join(item['currentPrice']))
            currentPrice = [e for e in re.split("[^0-9]", currentPrice) if e != '']
            item["currentPrice"]= "[" + currentPrice +"]"
        if item['originalPrice']:
            originalprice=("".join(item['originalPrice']))
            originalprice=[e for e in re.split("[^0-9]", originalprice) if e != '']
            item['originalPrice'] ="[" + str(min(map(int, originalprice))) + "]"
        if item['Category']:
            Category = ("".join(item['Category']))
            Category=re.sub(r'((\w+))', r'\1-', Category)
            item['Category'] = "[" + Category + "]"
        if item['Description']:
            item['Description'] = "[" + item['Description'] +"]"
        if item['PaginationImage']:
            PaginationImage = "[" +("".join(item['PaginationImage'])).replace('?$pdpthumb$',' ') +"]"
            item['PaginationImage'] = PaginationImage.replace('//anninc', 'http://anninc')
            return item

