# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from random import randint

class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?release_date=2019-01-01,&sort=num_votes,desc']

    def parse(self, response):
        all_movies = response.xpath('//div[@class="lister-item mode-advanced"]')
        for movie in all_movies:
            title = movie.xpath('normalize-space(.//h3/a/text())').extract_first()
            duration = movie.xpath('.//p[@class="text-muted "]/span[@class="runtime"]/text()').extract_first()
            genre = movie.xpath('normalize-space(.//p[@class="text-muted "]/span[@class="genre"]/text())').extract_first()
            imdb_rating = movie.xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract_first()
            metascore_rating = movie.xpath('normalize-space(.//div[@class="inline-block ratings-metascore"]/span/text())').extract_first()
            votes = movie.xpath('.//span[@name="nv"]/text()').extract_first()

            yield {
                'title': title,
                'duration': duration,
                'genre': genre,
                'imdb_rating': imdb_rating,
                'metascore_rating': metascore_rating,
                'votes': votes
            }

        sleep(randint(2, 5))

        next_page = response.xpath('//div[@class="desc"]/a/@href').extract_first()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
