import scrapy


class CondoinfoSpider(scrapy.Spider):
    name = 'condoinfo'
    allowed_domains = ['condos.ca']
    start_urls = ['https://condos.ca/toronto/condos-for-sale']

    def parse(self, response):
        condo_prices = response.xpath('//*[contains(@class, "styles___AskingPrice-sc-54qk44-4 dHPUdq")]/text()').getall()

        yield {
            'condo_prices': condo_prices
        }
