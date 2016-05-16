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

def post_job_to_server(item, logger=None):
    item = dict(item)
    url = "http://%s/rest/jobs/" % HOST
    user, pwd = 'root', 'root'
    # 检查是否存在
    params = {'positionId': item['positionId']}
    response = requests.get(url, params={'filter': json.dumps(params)})
    resp_json = response.json()
    # 存在
    if not resp_json['count']:
        params = dict(item)
        response = requests.post(url, json=params, auth=(user, pwd))
        if not response:
            sentry_client.captureMessage(json.dumps(params, indent=4, ensure_ascii=False))
            logger.error(params)
            logger.error(response.content)


def post_company_to_server(item, logger=None):
    item = dict(item)
    url = "http://%s/rest/company/" % HOST

    # 检查是否存在, 如果存在就用put, 不存在就用post
    cid = item['companyId']
    param = {'cid': cid}
    param = json.dumps(param)
    response = requests.get(url, params={'filter': param})
    resp_json = response.json()
    user, pwd = 'root', 'root'

    params = {
        "cid": cid,
        "name": item['companyName'],
        "address": "unknow",
        "companyShortName": item['companyShortName'],
        "companyName": item['companyName'],
        "financeStage": item['financeStage'],
        "companySize": item['companySize'],
        "lat":  item['lat'] or 0,
        "lng":  item['lng'] or 0,
        "score": item['score'],
        "briefPosition": item['briefPosition'],
        "detailPosition": item['detailPosition'],
    }
    # 存在
    if resp_json['count']:
        rid = resp_json['results'][0]['id']
        url = '%s%d/' % (url, rid)
        response = requests.patch(url, json=params, auth=(user, pwd))
    else:
        # 不存在
        response = requests.post(url, json=params, auth=(user, pwd))

    if not response.ok:
        sentry_client.captureMessage(json.dumps(params, indent=4, ensure_ascii=False))
        if logger:
            logger.error(params)
            logger.error(response.content)


class WorkCrawlerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, items.JobItem):
            post_job_to_server(item, logger=spider.logger)
        elif isinstance(item, items.CompanyItem):
            post_company_to_server(item, logger=spider.logger)
        return item

if __name__ == '__main__':
    item = {'briefPosition': u'\u5317\u4eac\u5e02\uff0c\u6d77\u6dc0\u533a',
             'companyId': 356,
             'companyName': u'\u6377\u901a\u534e\u58f0',
             'companyShortName': u'\u5317\u4eac\u6377\u901a\u534e\u58f0\u79d1\u6280\u80a1\u4efd\u6709\u9650\u516c\u53f8',
             'companySize': u'150-500\u4eba',
             'detailPosition': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u4e2d\u5173\u6751\u8f6f\u4ef6\u56ed2A\u697c2101',
             'financeStage': u'\u6210\u957f\u578b(\u4e0d\u9700\u8981\u878d\u8d44)',
             'lat': u'40.05486',
             'lng': u'116.303809',
             'score': u'3.5'}
    post_company_to_server(item)
