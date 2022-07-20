import scrapy


class CondoinfoSpider(scrapy.Spider):
    name = 'condoinfo'
    allowed_domains = ['condos.ca']
    start_urls = ['https://condos.ca/toronto/condos-for-sale']

    def parse(self, response):
        scrape_urls = []
        base_url = "https://condos.ca/toronto/condos-for-sale"
        
        for item in range(2,94):
            scrape_url = base_url + "?page=" + str(item)
            scrape_urls.append(scrape_url)
            

        for condo_entry in response.xpath("//div[@class = 'styles___PreviewContent-sc-54qk44-3 glSGVq']"):

            yield {
                'condo_prices': condo_entry.xpath(".//div[@class = 'styles___AskingPrice-sc-54qk44-4 dHPUdq']/text()").get(),
                'condo_address': condo_entry.xpath(".//address[@class = 'styles___Address-sc-54qk44-13 gTwVlm']/text()").get(),
                'beds' : condo_entry.xpath(".//div[@class = 'styles___InfoHolder-sc-54qk44-7 jtFhfz']/child::node()[1]").get(),
                'washrooms' : condo_entry.xpath(".//div[@class = 'styles___InfoHolder-sc-54qk44-7 jtFhfz']/child::node()[3]").get(),
                'parking' : condo_entry.xpath(".//div[@class = 'styles___InfoHolder-sc-54qk44-7 jtFhfz']/child::node()[7]").get(),
                'size' : condo_entry.xpath(".//div[@class = 'styles___Size-sc-54qk44-8 KRKbD']/text()").get(),
                'maintenance_fees': condo_entry.xpath(".//div[@class = 'styles___MaintHolder-sc-54qk44-10 laUWhE']/div/text()")[1].get(),
                'condo_ID': condo_entry.xpath(".//div[@class = 'styles___Mls-sc-54qk44-12 hRmahP']/text()")[1].get() 
            }

        for page in scrape_urls:
            yield scrapy.Request(url=page, callback =self.parse)