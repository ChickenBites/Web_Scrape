# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnntaylorItem(scrapy.Item):
    Category = scrapy.Field()
    URL = scrapy.Field()
    Title = scrapy.Field()
    PriceBeforeDiscount = scrapy.Field()
    PriceAfterDiscount = scrapy.Field()
    Colors = scrapy.Field()
    Sizes = scrapy.Field()
    Description = scrapy.Field()
    ItemId = scrapy.Field()
    Image = scrapy.Field()
    Material_And_Care = scrapy.Field()


