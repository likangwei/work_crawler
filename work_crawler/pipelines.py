# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import HOST
import requests
import json
import base64
from requests.auth import HTTPBasicAuth
import items


def post_job_to_server(item):
    item = dict(item)
    url = "http://%s/rest/jobs/" % HOST
    user, pwd = 'root', 'root'
    params = dict(item)
    response = requests.post(url, json=params, auth=(user, pwd))
    print response.content


def post_company_to_server(item):
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
        "lat":  item['lat'],
        "lng":  item['lng'],
        "score": item['score'],
        "briefPosition": item['briefPosition'],
        "detailPosition": item['detailPosition'],
    }
    # 存在
    if resp_json['count']:
        rid = resp_json['results'][0]['id']
        url = '%s%d/' % (url, rid)
        response = requests.put(url, json=params, auth=(user, pwd))
    else:
        # 不存在
        response = requests.post(url, json=params, auth=(user, pwd))
        print response.content


class WorkCrawlerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, items.JobItem):
            post_job_to_server(item)
        elif isinstance(item, items.CompanyItem):
            post_company_to_server(item)
        return item

if __name__ == '__main__':
    item = json.loads("""{"companyId":115639,
"positionName":"Python",
"positionType":"后端开发",
"workYear":"不限",
"education":"本科",
"jobNature":"全职",
"createTime":"2016-04-27 17:17:50",
"companyShortName":"北京凯博创盈科技发展有限公司",
"positionFirstType":"技术",
"positionId":1580725,
"salary":"8k-16k",
"city":"北京",
"positionAdvantage":"晋升空间",
"companyName":"北京凯博创盈科技发展有限公司",
"companyLogo":"i/image/M00/06/EB/Cgp3O1bNXnOAb0JEAAAHYPkPBTc687.png",
"industryField":"移动互联网 · 数据服务",
"financeStage":"初创型(未融资)",
"companyLabelList":[],
"leaderName":"暂没有填写",
"companySize":"15-50人",
"deliverCount":3,
"score":1208,
"adjustScore":0,
"relScore":1000,
"formatCreateTime":"1天前发布",
"randomScore":0,
"countAdjusted":false,
"calcScore":false,
"orderBy":60,
"showOrder":0,
"haveDeliver":false,
"adWord":0,
"createTimeSort":1461748670000,
"positonTypesMap":null,
"hrScore":62,
"flowScore":86,
"showCount":238,
"pvScore":48.04361074035268,
"plus":"否",
"imstate":"disabled",
"totalCount":0,
"searchScore":0.0}""")
    post_job_to_server(item)
