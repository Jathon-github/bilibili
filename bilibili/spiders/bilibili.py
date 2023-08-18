import json
import re

from bilibili.items import BilibiliItem
from scrapy.spiders import Request
from scrapy.spiders import Spider
from scrapy.utils.project import get_project_settings


settings = get_project_settings()


class Bilibili(Spider):
    name = 'bilibili'

    def start_requests(self):
        url = 'https://www.bilibili.com/video/' + settings['VIDEO_AID']
        yield Request(url)

    def parse(self, response, **kwargs):
        parts = re.findall(r'"part":"(.*?)"', response.text)

        for i, part in enumerate(parts):
            item = BilibiliItem()
            item['title'] = f'{i + 1}. {part}'
            yield Request(
                url=f'{response.url}?p={i + 1}',
                callback=self.pages_parse,
                meta={'item': item},
            )

    def pages_parse(self, response, **kwargs):
        dash = json.loads(
            re.search(r'__playinfo__=(.*?)</script>', response.text).group(1)
        )['data']['dash']
        item = response.meta['item']

        item['file_urls'] = [
            dash['video'][0]['baseUrl'],
            dash['audio'][0]['baseUrl'],
        ]

        yield item
