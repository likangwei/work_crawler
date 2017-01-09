# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import HOST
from settings import sentry_client
import requests
import json
import base64
from requests.auth import HTTPBasicAuth
import items
import sys




class WorkCrawlerPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except:
            pass
        return item

