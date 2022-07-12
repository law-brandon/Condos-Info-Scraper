import scrapy


class CondoinfoSpider(scrapy.Spider):
    name = 'condoinfo'
    allowed_domains = ['condos.ca']
    start_urls = ['https://condos.ca/toronto/condos-for-sale']

    def parse(self, response):
        condo_prices = response.xpath('//*[contains(@class, "styles___AskingPrice-sc-54qk44-4 dHPUdq")]/text()').getall()
        condo_addresses = response.xpath('//*[contains(@class, "styles___Address-sc-54qk44-13 gTwVlm")]/text()').getall()
        condo_specs = response.xpath('//*[contains(@class, "styles___InfoHolder-sc-54qk44-7 jtFhfz")]/text()').getall()
        condo_size = response.xpath('//*[contains(@class, "styles___Size-sc-54qk44-8 KRKbD")]/text()').getall()
        #maint_fee = response.xpath('//*[contains(@class, "styles___MaintHolder-sc-54qk44-10 laUWhE")]/text()').getall()
        condo_ID = response.xpath('//*[contains(@class, "styles___Mls-sc-54qk44-12 hRmahP")]/text()').getall()

        yield {
            'condo_prices': condo_prices,
            'condo_addresses' : condo_addresses,
            'condo_specs' : condo_specs,
            'condo_size' : condo_size,
            #'maint_fee' : maint_fee,
            'condo_ID' : condo_ID
        }
