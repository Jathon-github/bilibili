# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
from scrapy.spiders import Request
from scrapy.pipelines.files import FilesPipeline as ScrapyFilesPipeline
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
store = settings['FILES_STORE']


class FilesPipeline(ScrapyFilesPipeline):
    def get_media_requests(self, item, info):
        headers = {'Referer': 'https://www.bilibili.com/'}
        urls = ItemAdapter(item).get(self.files_urls_field, [])
        return [Request(u, headers=headers) for u in urls]


class BilibiliPipeline:
    def process_item(self, item, spider):
        title = item['title']
        video_path = '%s%s.mp4' % (store, title)
        cmd_str = ''.join([
            '-i %s%s ' % (store, file['path'])
            for file in item['files']
        ])
        os.system('ffmpeg %s -c copy %s' % (cmd_str, video_path))
