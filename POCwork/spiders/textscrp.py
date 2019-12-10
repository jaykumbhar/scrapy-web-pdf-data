from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
# from Scrapy_One.items import Items_Main

class MySpider(CrawlSpider):
    name = 'spiderName'
    allowed_domains = ['example.de']
    start_urls = ['https://www.businesswire.com/news/home/20180531005074/en/']
    rules = (Rule(LinkExtractor(allow = ('', ),
                            deny = ('/(\w|\W)*([Ii]mpressum|[Aa]bout|[Pp]rivacy|[Tt]erms|[Cc]opyright|[Hh]elp|[Hh]ilfe|[Dd]atenschutz|[KkCc]onta[kc]t|[Rr]echtliche(\w|\W)*[Hh]inweis|[Hh]aftungsausschlu)'),
                            unique = True),
                            callback = 'parse_stuff',
                            follow = True),
        )

    def parse_stuff(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//body')
        items_main = []

        for site in sites:
            loader = ItemLoader(item = Items_Main(), response = response)
            loader.add_xpath('fragment', '//*[not(self::script)]/text()')
            items_main.append(loader.load_item())
            return items_main