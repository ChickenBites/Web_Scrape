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
            item["currentPrice"]= str(min(map(int, currentPrice)))
        if item['originalPrice']:
            originalprice=("".join(item['originalPrice']))
            originalprice=[e for e in re.split("[^0-9]", originalprice) if e != '']
            item['originalPrice'] = str(min(map(int, originalprice)))
        if item['Category']:
            Category = ("".join(item['Category']))
            item["Category"]=re.sub(r'>', '->', Category)
        if item["Colors"]:
            Colors=['" ' + color + '"' for color in item["Colors"]]
            Colors=(",".join(Colors))
            item["Colors"]="[" + Colors + "]"
        if item["Sizes"]:
            Sizes = ['" ' + size + '"' for size in item["Sizes"]]
            Sizes = (",".join(Sizes))
            item["Sizes"] = "[" + Sizes + "]"
            if item["PaginationImages"]:
                Images = ['" ' + image + '"' for image in item["PaginationImages"]]
                Images = (",".join(Images))
                item["PaginationImages"] = "[" + Images + "]"
        if item['PaginationImages']:
            PaginationImages = ("".join(item['PaginationImages'])).replace('?$pdpthumb$','')
            item['PaginationImages'] = "[" + PaginationImages.replace('//anninc', 'http://anninc') +"]"
        return item

