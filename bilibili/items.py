# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    video_url = scrapy.Field()
    audio_url = scrapy.Field()
    video_stream = scrapy.Field()
    audio_stream = scrapy.Field()
