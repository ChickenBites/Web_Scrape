# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
#
# class AnntaylorPipeline(object):
#     def open_spider(self, spider):
#         self.f = open("anntaylor.json", 'w')
#
#     def process_item(self, item, spider):
#         item = json.dumps(dict(item), ensure_ascii=False)
#         self.f.write(item + ',\n')
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()