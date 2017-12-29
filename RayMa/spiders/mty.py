# -*- coding: utf-8 -*-
import scrapy
from RayMa.items import RaymaItem

class MtySpider(scrapy.Spider):
    name = 'mty'
    allowed_domains = ['tieba.baidu.com/p/5071688062','tieba.baidu.com']   # Filtered offsite request to 'tieba.baidu.com'
    start_urls = ['http://tieba.baidu.com/p/5071688062']

    def parse(self, response):
        item={}
        imgurl=[]
        imgurl=response.xpath('//cc//img[@class="BDE_Image"]/@src').extract()
        item=RaymaItem()
        item['image_urls']=imgurl
        yield item
        nexturl=response.xpath('//div[@class="pb_footer"]//ul[@class="l_posts_num"]//a/@href').extract()
        if nexturl:
            url='http://tieba.baidu.com/p/5071688062'+nexturl[-2]
            yield scrapy.Request(url,callback=self.parse)
