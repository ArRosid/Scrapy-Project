# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderCssSpider(scrapy.Spider):
    name = 'quotes_spider_css'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        all_quotes = response.css('.quote')
        for quote in all_quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('div.tags > a.tag::text').extract()
            # tags = quote.css('.tag::text').extract()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        next_page = response.css('.next > a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
