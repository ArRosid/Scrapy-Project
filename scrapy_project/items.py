# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class ImdbItem(scrapy.Item):
    title = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    imdb_rating = scrapy.Field()
    metascore_rating = scrapy.Field()
    votes = scrapy.Field()
