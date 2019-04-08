# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#
#
class AnntaylorItem(scrapy.Item):
    Category = scrapy.Field()
    url = scrapy.Field()
    Title = scrapy.Field()
    originalPrice = scrapy.Field()
    currentPrice = scrapy.Field()
    Colors = scrapy.Field()
    Sizes = scrapy.Field()
    Description = scrapy.Field()
    ItemId = scrapy.Field()
    PaginationImages = scrapy.Field()
    Material_And_Care = scrapy.Field()


