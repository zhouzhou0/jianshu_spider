# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        item = ArticleItem()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        item['title'] = response.xpath("//div[@class='article']/h1/text()").get()
        item['author'] =response.xpath("//div[@class='info']/span[@class='name']/a/text()").get()
        item['avatar'] = response.xpath("//div[@class='author']/a[@class='avatar']/img/@src").get()
        item['content'] = response.xpath("//div[@class='show-content-free']").get()
        item['pub_time'] = response.xpath("//span[@class='publish-time']/text()").get().replace('*','')

        # https://www.jianshu.com/p/f0c5934b5d3f?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
        # https://www.jianshu.com/p/f03e0080e3e5
        item['article_id'] = response.url.split('?')[0].split('/')[-1]
        item['origin_url'] = response.url
        item['word_count'] = response.xpath("//span[@class='wordage']/text()").get()
        item['read_count'] = response.xpath("//span[@class='views-count']/text()").get()
        item['like_count'] = response.xpath("//span[@class='likes-count']/text()").get()
        item['comment_count'] = response.xpath("//span[@class='comments-count']/text()").get()
        subject =response.xpath("//div[@class='include-collection']/a//div[contains(@class,'name')]/text()").getall()
        item['subject'] =','.join(subject)





        print(item)
        yield item
