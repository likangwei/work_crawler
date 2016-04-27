# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from scrapy.http import Request
from work_crawler.items import JobItem


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
            "first": "true" if pn == 1 else "false",
            "pn": pn,
            "kd": "python"
        }
        body = json.dumps(param)
        request = Request(url, method="POST", body=body, dont_filter=True)
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
                item['source'] = company
                yield item

            if has_next_pg:
                self.logger.info('has next page')
                request = self.get_request_by_pg(int(pg_no) + 1)
                yield request
