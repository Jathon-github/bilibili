import json
import re

from bilibili.items import BilibiliItem
from scrapy import Request
from scrapy.spiders import Spider
from scrapy.utils.project import get_project_settings
from scrapy_splash.request import SplashRequest


settings = get_project_settings()
headers = {'Referer': 'https://www.bilibili.com/'}


class Bilibili(Spider):
    name = 'bilibili'

    def start_requests(self):
        url = 'https://www.bilibili.com/video/' + settings['VIDEO_AID']
        yield SplashRequest(
            url,
            args={
                'wait': self.settings['TIME_LIMIT'],
                'images': 0,
            }
        )

    def parse(self, response, **kwargs):
        list_box = response.xpath('//ul[@class="list-box"]/li')

        for box in list_box:
            detail_url = response.urljoin(box.xpath('./a/@href').extract_first())
            title = box.xpath('./a//span[@class="part"]/text()').extract_first()

            item = BilibiliItem()
            item['title'] = title

            yield SplashRequest(
                detail_url,
                callback=self.detail_parse,
                meta={'item': item},
                args={
                    'wait': self.settings['TIME_LIMIT'],
                    'images': 0,
                }
            )

    def detail_parse(self, response, **kwargs):
        detail_info = json.loads(re.search(r'__playinfo__=(.*?)</script>', response.text).group(1))
        item = response.meta['item']

        item['video_url'] = detail_info['data']['dash']['video'][0]['baseUrl']
        item['audio_url'] = detail_info['data']['dash']['audio'][0]['baseUrl']

        yield Request(item['video_url'], headers=headers, callback=self.video_parse, meta={'item': item})

    def video_parse(self, response, **kwargs):
        item = response.meta['item']
        item['video_stream'] = response.body
        yield Request(item['audio_url'], headers=headers, callback=self.audio_parse, meta={'item': item})

    def audio_parse(self, response, **kwargs):
        item = response.meta['item']
        item['audio_stream'] = response.body
        yield item
