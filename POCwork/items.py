# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from .pipelines import PocworkPipeline
class PocworkItem(scrapy.Item):
    # define the fields for your item here like:
    # contact = scrapy.Field()
    date = scrapy.Field()
    websiteContent = scrapy.Field()
    website = scrapy.Field()
    # pass

