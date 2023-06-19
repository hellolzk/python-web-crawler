# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主播名称
    name=scrapy.Field()
    #房间名称
    rommname = scrapy.Field()
    #封面图片
    picture=scrapy.Field()
    #房间热度
    redu=scrapy.Field()