# -*- coding: utf-8 -*-
import scrapy
from ..items import ImdbItem

class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?release_date=2019-01-01,&sort=num_votes,desc']

    def parse(self, response):
        items = ImdbItem()

        all_movies = response.xpath('//div[@class="lister-item mode-advanced"]')
        for movie in all_movies:
            items['title'] = movie.xpath('.//h3/a/text()').extract_first()
            items['duration'] = movie.xpath('.//p[@class="text-muted "]/span[@class="runtime"]/text()').extract_first()
            items['genre'] = movie.xpath('.//p[@class="text-muted "]/span[@class="genre"]/text()').extract_first()
            items['imdb_rating'] = movie.xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract_first()
            items['metascore_rating'] = movie.xpath('.//div[@class="inline-block ratings-metascore"]/span/text()').extract_first()
            items['votes'] = movie.xpath('.//span[@name="nv"]/text()').extract_first()

            yield items
