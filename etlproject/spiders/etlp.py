import scrapy
from ..items import EtlprojectItem

class EtlpSpider(scrapy.Spider):
    name = "etl"
    page_no=2
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/laptops"]

    def parse(self, response):
        for product in response.css('div.thumbnail'):
            items = EtlprojectItem()
            items['product_name'] = product.css('.title::text').get(default='').strip()
            items['product_price'] = product.css('h4.price span[itemprop="price"]::text').get(default='').strip()
            items['product_description'] = product.css('.card-text::text').get(default='').strip()
            items['product_reviews']=product.css('p.float-end span[itemprop="reviewCount"]::text').get(default='').strip()
            yield items
        next_page='https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='+str(EtlpSpider.page_no)
        if EtlpSpider.page_no <=20:
            EtlpSpider.page_no+=1
            yield response.follow(next_page, callback=self.parse)



