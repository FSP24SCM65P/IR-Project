import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'my_spider'
    
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
        self.max_pages = int(kwargs.get('max_pages'))
        self.max_depth = int(kwargs.get('max_depth'))

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        if self.max_pages > 0 and len(self.crawler.engine.slot.inprogress) >= self.max_pages:
            self.crawler.engine.close_spider(self, 'Reached maximum pages limit')
        elif response.request.meta.get('depth') >= self.max_depth:
            self.crawler.engine.close_spider(self, 'Reached maximum depth limit')

from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

settings = Settings({
    'AUTOTHROTTLE_ENABLED': True,
    'DOWNLOAD_DELAY': 0.5,
})

if __name__ == "__main__":
    process = CrawlerProcess(settings=settings)
    process.crawl(MySpider, start_url='https://en.wikipedia.org/wiki/Main_Page', max_pages=10, max_depth=3)
    process.start()
