# -*- coding: utf-8 -*-
import json

import scrapy
from FigureScrapy.items import FigurescrapyItem


class FigureSpider(scrapy.Spider):
    name = 'figure'
    # allowed_domains = ['itcast.cn']
    # 中国艺人
    # start_urls = ['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=500&format=json&ie=utf-8&oe=utf-8&query=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&rn=100&_=1580457480665&pn=' + str(x) for x in range(0, 12 * 3238, 100)]
    # start_urls = ['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=500&format=json&ie=utf-8&oe=utf-8&query=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&rn=100&_=1580457480665&pn=0']
    start_urls = ['']
    def parse(self, response):
        # 参考链接：https://www.runoob.com/w3cnote/scrapy-detail.html
        # 存放信息的集合
        items = []
        js = json.loads(response.body)
        figs = js['data'][0]['result']
        for fig in figs:
            item = FigurescrapyItem()
            name = fig['ename']
            url = fig['pic_4n_78']
            baike_url = fig['url']
            item['keyword'] = '中国艺人'
            item['title'] = name
            item['img_url'] = url
            item['baike_url'] = baike_url

            yield item
        #     items.append(item)
        #
        # # 直接返回最后数据
        # return items
