# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from scrapy.http import Request
from work_crawler.items import JobItem

cookies = {
    "LGUID": r'20160220235342-1db33639-d7ea-11e5-8af7-525400f775ce',
    "user_trace_token": r'20160220235343-3f869358a02f4b10b8c41c70b8cc8240',
    "tencentSig": r'7998688256',
    "LGMOID": r'20160427233631-95B62C60BAF6E21621017A305D0ED578',
    "login": r'true',
    "unick": r'%E6%9D%8E%E5%BA%B7%E7%82%9C',
    "index_location_city": r'%E5%8C%97%E4%BA%AC',
    "JSESSIONID": r'7F8241BAA191D456D34902BB643C5502',
    "_gat": r'1',
    "PRE_UTM": r'',
    "PRE_HOST": r'',
    "PRE_SITE": r'',
    "PRE_LAND": r'http%3A%2F%2Fwww.lagou.com%2F',
    "LGSID": r'20160507205357-c3570036-1452-11e6-9d6c-525400f775ce',
    "LGRID": r'20160507205405-c79e6b44-1452-11e6-95eb-5254005c3644',
    "SEARCH_ID": r'bdb56adf40fa4abe83d9d8e1159d0d0c',
    "_ga": r'GA1.2.1691610691.1455983623',
    "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": r'1461771393,1461778531',
    "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": r'1462625661',
}

header = {
    "Cookie": r'LGUID=20160220235342-1db33639-d7ea-11e5-8af7-525400f775ce; user_trace_token=20160220235343-3f869358a02f4b10b8c41c70b8cc8240; tencentSig=7998688256; LGMOID=20160427233631-95B62C60BAF6E21621017A305D0ED578; login=true; unick=%E6%9D%8E%E5%BA%B7%E7%82%9C; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=7F8241BAA191D456D34902BB643C5502; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=http%3A%2F%2Fwww.lagou.com%2F; LGSID=20160507205357-c3570036-1452-11e6-9d6c-525400f775ce; LGRID=20160507205405-c79e6b44-1452-11e6-95eb-5254005c3644; SEARCH_ID=bdb56adf40fa4abe83d9d8e1159d0d0c; _ga=GA1.2.1691610691.1455983623; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1461771393,1461778531; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1462625661',
    "Origin": r'http://www.lagou.com',
    "Accept-Encoding": r'gzip, deflate',
    "Host": r'www.lagou.com',
    "Accept-Language": r'zh-CN,zh;q=0.8',
    "User-Agent": r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36',
    "Content-Type": r'application/x-www-form-urlencoded; charset=UTF-8',
    "Accept": r'application/json, text/javascript, */*; q=0.01',
    "Referer": r'http://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    "X-Requested-With": r'XMLHttpRequest',
    "Connection": r'keep-alive',
}


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def get_request_by_pg(self, pn):
        param = {"city": "北京"}
        url = "http://www.lagou.com/jobs/positionAjax.json?%s" % urllib.urlencode(param)
        param = {
            "first": "true" if int(pn) == 1 else "false",
            "pn": str(pn),
            "kd": "python"
        }
        body = urllib.urlencode(param)
        request = Request(url, headers=header, cookies=cookies, method="POST", body=body, dont_filter=True)
        return request

    def start_requests(self):
        yield self.get_request_by_pg(1)

    def parse(self, response):

        data = json.loads(response.body)
        if data['success']:
            content = data['content']
            has_next_pg = content['hasNextPage']
            pg_no = content['pageNo']
            results = content['result']
            for company in results:
                item = JobItem()
                item.update(company)
                yield item

            if has_next_pg:
                self.logger.info('has next page')
                request = self.get_request_by_pg(int(pg_no) + 1)
                yield request
