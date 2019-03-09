# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnntaylorItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    # sale_price = scrapy.Field()
    colors = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()



