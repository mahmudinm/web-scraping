# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    images = scrapy.Field()
    image_dir = scrapy.Field()
    image_names = scrapy.Field()
    image_urls = scrapy.Field()