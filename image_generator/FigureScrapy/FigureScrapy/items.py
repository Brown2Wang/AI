# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FigurescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    baike_url = scrapy.Field()
    # img_res = scrapy.Field()

