# part 5: scrapy
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import TutorialItem
from scrapy.loader import ItemLoader


class ProductsSpide(CrawlSpider):
    name = 'products'
    allowed_domains = ['rei.com']
    start_urls = ['https://www.rei.com/c/camping-and-hiking/f/scd-deals']

    rules = (
        Rule(LinkExtractor(allow=(r'page=',))),
        Rule(LinkExtractor(allow=(r'product', )), callback='parse_item'),
              
    )

    def parse_item(self, response):
        l = ItemLoader(item=TutorialItem(), response=response)
        l.add_css('title', 'h1#product-page-title')
        l.add_css('price', 'span#buy-box-product-price')
        l.add_css('item_no', 'span#product-item-number')
        l.add_css('rating', 'span.cdr-rating__number_13-5-3')

        return l.load_item()
