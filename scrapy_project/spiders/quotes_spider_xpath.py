# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesItem


class QuotesSpiderXpathSpider(scrapy.Spider):
    name = 'quotes_spider_xpath'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        items = QuotesItem()

        all_quotes = response.xpath('//div[@class="quote"]')
        for quote in all_quotes:
            items['text'] = quote.xpath('./span[@class="text"]/text()').extract_first()
            items['author'] = quote.xpath('.//small/text()').extract_first()
            items['tags'] = quote.xpath('.//a[@class="tag"]/text()').extract()

            yield items

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
