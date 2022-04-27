# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import os
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
store = settings['FILES_STORE']


class BilibiliPipeline:
    def process_item(self, item, spider):
        title = item['title']
        video_path = '%s/video/%s.mp4' % (store, title)
        audio_path = '%s/audio/%s.mp4' % (store, title)
        path = '%s/%s.mp4' % (store, title)

        with open(video_path, 'wb') as video:
            video.write(item['video_stream'])
        with open(audio_path, 'wb') as audio:
            audio.write(item['audio_stream'])

        os.system('ffmpeg -i %s -i %s -c copy %s' % (video_path, audio_path, path))


if not os.path.exists(store + '/video'):
    os.makedirs(store + '/video')
if not os.path.exists(store + '/audio'):
    os.makedirs(store + '/audio')
