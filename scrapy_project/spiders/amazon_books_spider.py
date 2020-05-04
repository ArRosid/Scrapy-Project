# -*- coding: utf-8 -*-
import scrapy


class AmazonBooksSpiderSpider(scrapy.Spider):
    name = 'amazon_books_spider'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A618073011&s=review-count-rank&dc&fst=as%3Aoff&qid=1588545134&rnid=618072011&ref=sr_pg_2']

    def parse(self, response):
        print(response)
        all_books = response.xpath('//div[@class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]')
        for book in all_books:
            title = book.xpath('.//h2//span/text()').extract_first()
            author = book.xpath('.//a[@class="a-size-base a-link-normal"]/text()').extract_first()
            rating = book.xpath('.//span[@class="a-icon-alt"]/text()').extract_first()
            vote = book.xpath('.//a[@class="a-link-normal"]/span/text()').extract_first()
            kindle_price = book.xpath('.//span[@class="a-offscreen"]/text()').extract_first()

            yield {
                'title': title,
                'author': author,
                'rating': rating,
                'vote': vote,
                'kindle_price': kindle_price
            }
