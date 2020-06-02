# -*- coding: utf-8 -*-
import scrapy
from ..items import BaytTutorialItem

class BaytSpiderSpider(scrapy.Spider):
    name = 'bayt_spider'
    start_urls = ['https://www.bayt.com/en/uae/jobs/q/accountant/']

    def parse(self, response):
        items = BaytTutorialItem()
        for jobs in response.css('li.has-pointer-d'):
            job = jobs.css('.t-regular a::text').extract_first()
            items['job_name'] = job.strip()
            Company = jobs.css('.p10r::text').extract_first()
            items['company'] = Company.strip()
            date = jobs.css('div.t-small::text').extract()[1]
            items['Date'] = date.strip()
            yield items

        next=response.css('li.pagination-next a::attr(href)').get()
        if next is not None:
            next_page = next.split('/')[-1]
            yield response.follow(next_page, callback= self.parse)



        #for jobs in response.css('.t-regular a::text').extract():
            #job_name = jobs.strip()
            #items['job_name'] = job_name
            #items['company'] = response.css('.p10r::text').extract()
            #yield items
        #job_name = response.css('.t-regular a::text').extract_first().strip()
        #for companies in response.css('.p10r::text').extract():
        #    items['company'] = companies.strip().replace('\t','')
        #    yield items
