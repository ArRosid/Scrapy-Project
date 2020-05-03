# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderXpathSpider(scrapy.Spider):
    name = 'quotes_spider_xpath'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        all_quotes = response.xpath('//div[@class="quote"]')
        for quote in all_quotes:
            text = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quote.xpath('.//small/text()').extract_first()
            tags = quote.xpath('.//a[@class="tag"]/text()').extract()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
