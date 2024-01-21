
from scrapy_app.items import ScrapyQuote
import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"

    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    # this is what start_urls does
    # def start_requests(self):
    #     urls = ['https://www.theodo.co.uk/team',]
    #     for url in urls:
    #       yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = ScrapyQuote()
            item['text'] = quote.css("span.text::text").extract_first()
            item['author'] = quote.css("small.author::text").extract_first()
            yield item
