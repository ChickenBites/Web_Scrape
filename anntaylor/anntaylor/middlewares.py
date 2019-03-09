from time import sleep
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Anntaylor_selenium_middleware(object):
    def __init__(self):
        # option = Options()
        # option.set_headless()
        self.driver = webdriver.Chrome(r'C:\Users\guyz\PycharmProjects\Web_scrape\anntaylor\chromedriver.exe')
        # self.driver = webdriver.PhantomJS()

    def process_request(self, spider, request):
        self.driver.implicitly_wait(5)
        self.driver.get(request.url)
        body = self.driver.page_source

        return HtmlResponse(url=self.driver.current_url,
                            body=body,
                            encoding='utf-8',
                            request=request)
    def __del__(self):
        self.driver.quit()
