# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from anntaylor.items import AnntaylorItem

# from scrapy.http import Request
# from scrapy.loader import ItemLoader
# from scrapy_splash import SplashRequest
class AnntaylorSpider(CrawlSpider):
        name='anntaylor'
        allowed_domains=['anntaylor.com',]
        # start_urls=('https://www.anntaylor.com',)
        start_urls = ['https://www.anntaylor.com/all-clothing/cat3630020',
                      'https://www.anntaylor.com/work/cat2100002',
                      'https://www.anntaylor.com/shoes-view-all/cata000020',
                      'https://www.anntaylor.com/accessories-view-all/cata000025',
                      'https://www.anntaylor.com/petites/cata00004',
                      'https://www.anntaylor.com/tall/cat140002',
                      'https://www.anntaylor.com/all-luxewear/cat3750001',
                      'https://www.anntaylor.com/at-the-moment/cat2600064',
                      'https://www.anntaylor.com/sale/cata00007',]
        # for url in start_urls:
        rules = (Rule(LinkExtractor(allow = ('skuId=.*',)), follow=True, callback="parse_item"),)
        # , deny =('/cat.*',))
        # allow = ('skuId=.*',)
                # Rule(LinkExtractor(canonicalize=True, unique=True),follow=True, callback="parse_item")


        #Use Splash#

        # def start_requests(self):
        #
        #     url='https://www.anntaylor.com/clip-dot-chiffon-full-skirt/489812?skuId=26892825&defaultColor=2222&catid=cata000016'
        #
        #     yield SplashRequest(
        #         url=url,
        #         callback=self.parse_item,
        #         endpoint='render.html',
        #         args={'wait':3},
        # def __init__(self):
        #     )
        #     self.driver = webdclsriver.Firefox()
        #



        def parse_item(self, response):
            item=AnntaylorItem()
            item["Category"] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "breadcrumb-plp", " " ))]//span//text()').extract()
            url= response.xpath('//link[@rel="canonical"]/@href').extract()
            item["URL"]=url
            urljoin=("".join(url))
            item["ItemId"] = urljoin.split('/')[-1]
            item["Title"] = response.xpath('//h1/text()').extract()
            item["PriceBeforeDiscount"] = response.xpath('//strong[@class="price"]//span//text()').extract()
            item["PriceAfterDiscount"] = response.xpath('//strong[@class="price sale"]//span/text()').extract()
            item["Colors"] = response.css('.color-button::text').extract()
            item["Sizes"] = response.xpath('//fieldset[@class="sizes"]//div[@tabindex="-1"]//a/text()').extract()
            item["Image"] = response.xpath('//div[@class="swiper-slide main-image swiper-slide-visible swiper-slide-active"]//span[@tabindex="-1"]//img/@src').extract()
            item["Description"] = response.xpath('//span[@class="description"]/text() | //span[@class="bullet-point-panel"]/text() | //span[@class="color-families"]/text()').extract()
            item["Material_And_Care"] = response.xpath('//span[@class="list-item"]/text()').extract()
            yield item
