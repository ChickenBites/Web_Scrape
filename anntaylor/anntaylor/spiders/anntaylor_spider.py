# -*- coding: utf-8 -*-
import scrapy
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
        # def start_requests(self):
        #      for url in self.start_urls:
        #         yield Request(url=url, callback=self.parse_item)

        # def parse(self,response):
        #
        #     pass

        def parse_item(self, response):
            item=AnntaylorItem()
            item["category"] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "breadcrumb-plp", " " ))]//span//text()').extract()
            item["url"] = response.xpath('//link[@rel="canonical"]/@href').extract()
            item["title"] = response.xpath('//h1/text()').extract()
            item["price"] = response.xpath('//strong[@class="price"]//span//text()| //*[contains(concat( " ", @class, " " ), concat( " ", "sale", " " ))]//span//text()| //*[contains(concat( " ", @class, " " ), concat( " ", "range", " " ))]//span//text() ').extract()
            # item["sale_price"] = response.css('.sale span::text').extract()
            # item["prices"] = response.xpath('//*[contains(concat(" ", @class, " " ), concat( " ", "sale-price", " " ))]//text() | //*[contains(concat( " ", @class, " " ), concat( " ", "price-marked", " " ))]//text() | //*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]//text() ').extract()
            item["colors"] = response.css('.color-button::text').extract()
            item["sizes"] = response.css('div.product-details.component:nth-child(2) section.product-information.component form.customizer fieldset.sizes:nth-child(10) > div:nth-child(2) > a::text').extract()
            # item["description"] = response.xpath('//*[contains(concat( " ", @clasexits, " " ), concat( " ", "color-families", " " ))]/text() | //*[contains(concat( " ", @class, " " ), concat( " ", "bullet-point-panel", " " ))]/text() | //*[contains(concat( " ", @class, " " ), concat( " ", "list-item", " " ))]/text() | //*[contains(concat( " ", @class, " " ), concat( " ", "description", " " ))]/text() | //*[(@id = "details-panel")]//strong/text()').extract()
            item["description"]=response.css('#details-panel span::text').extract()
            yield item
