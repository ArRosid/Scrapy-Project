# -*- coding: utf-8 -*-
import scrapy


class IndeedProgrammerSpiderSpider(scrapy.Spider):
    name = 'indeed_programmer_spider'
    allowed_domains = ['id.indeed.com']
    start_urls = ['https://id.indeed.com/jobs?q=programmer&sort=date']

    def parse(self, response):
        all_jobs = response.xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result"]')
        for job in all_jobs:
            job_title = job.xpath('.//h2/a/descendant::text()').extract()
            job_title = ' '.join([title.strip() for title in job_title])
            company_name = job.xpath('normalize-space(.//span[@class="company"]/text())').extract_first()
            location = job.xpath('normalize-space(.//span[@class="location accessible-contrast-color-location"]/text())').extract_first()
            salary = job.xpath('normalize-space(.//span[@class="salaryText"]/text())').extract_first()
            posted = job.xpath('normalize-space(.//span[@class="date "]/text())').extract_first()

            yield {
                'job_title': job_title,
                'company_name': company_name,
                'location': location,
                'salary': salary,
                'posted': posted
            }

        next_page = response.xpath('//a[@aria-label="Next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
