# -*- coding: utf-8 -*-
import scrapy


class JustiaBusinessLawyersCaliforniaSpiderSpider(scrapy.Spider):
    name = 'justia_business_lawyers_california_spider'
    allowed_domains = ['www.justia.com']
    start_urls = ['https://www.justia.com/lawyers/business-law/california/']

    def parse(self, response):
        all_lawyers = response.xpath('//div[@class="jcard lawyer-card lawyer-card-status--premium -gold"]')
        for lawyer in all_lawyers:
            name = lawyer.xpath('.//strong[@class="name lawyer-name -hide-tablet"]//span/text()').extract_first()
            city = lawyer.xpath('normalize-space(.//p[@class="has-no-top-margin"]/text())').extract_first()
            experience = lawyer.xpath('.//span[@class="nowrap"]/text()').extract_first()
            phone_number = lawyer.xpath('.//li[@class="-phone"]/a/text()').extract_first()
            website_url = lawyer.xpath('.//a[@class="button button-radius button-ghost"]/@href').extract_first()
            profile_url = lawyer.xpath('.//a[@class="button button-radius button-ghost -hide-desktop"]/@href').extract_first()

            yield {
                'name': name,
                'city': city,
                'experience': experience,
                'phone_number': phone_number,
                'website_url': website_url,
                'profile_url': profile_url
            }

        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
