# -*- coding: utf-8 -*-
import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = 'newsSpider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/r/worldnews/rising/']

    custom_settings = {
        'DEPTH_LIMIT': 10000
    }

    def parse(self, response):
        titles = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]/text()').extract()
        datetimes = response.xpath('//*[@data-click-id="timestamp"]/text()').extract()
        links = response.xpath('//*[@class="_13svhQIUZqD9PVzFcLwOKT styled-outbound-link"]/text()').extract()
        for (title, link, datetime) in zip(titles, links, datetimes):
            yield {'Title': title.encode('utf-8'), 'News Link': link, 'Date Time': datetime}

        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
