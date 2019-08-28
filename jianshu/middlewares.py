# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.dirver = webdriver.Chrome()


    def process_request(self,request,spider):
        self.dirver.get(request.url)
        time.sleep(1)
        try:
            while True:
                showMore = self.dirver.find_element_by_class_name('show-more')
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass
        source = self.dirver.page_source
        response = HtmlResponse(url=self.dirver.current_url,body=source,request=request,encoding="utf-8")
        return response

