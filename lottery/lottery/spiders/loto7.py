import scrapy


class Loto7Spider(scrapy.Spider):
    name = 'loto7'
    allowed_domains = ['www.mizuhobank.co.jp']
    start_urls = ['http://www.mizuhobank.co.jp/']

    def parse(self, response):
        pass
