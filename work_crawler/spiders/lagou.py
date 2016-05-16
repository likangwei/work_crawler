# -*- coding: utf-8 -*-
import scrapy
import json
import re
import urllib
from scrapy.http import Request
from work_crawler.items import JobItem
from work_crawler.items import CompanyItem

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
        if pn > 30:
            return None

        param = {"city": "北京"}
        url = "http://www.lagou.com/jobs/positionAjax.json?%s" % urllib.urlencode(param)
        param = {
            "first": "true" if int(pn) == 1 else "false",
            "pn": str(pn),
            "kd": "python"
        }
        body = urllib.urlencode(param)
        request = Request(url, headers=header, cookies=cookies, method="POST", body=body, dont_filter=True)
        request.meta['pn'] = pn
        return request

    def get_company_request(self, company_item):
        cid = company_item['companyId']
        url = 'http://www.lagou.com/gongsi/%s.html' % cid
        request = Request(url, callback=self.parse_company)
        request.meta['company_item'] = company_item
        return request

    def start_requests(self):
        yield self.get_request_by_pg(1)

    def parse(self, response):
        self.log(response.body)
        data = json.loads(response.body)
        if data['success']:
            content = data['content']
            positionResult = content['positionResult']
            pg_no = response.request.meta['pn']
            results = positionResult['result']
            for result in results:
                item = JobItem()
                item['companyId'] = result['companyId']
                item['positionName'] = result['positionName']
                item['positionType'] = result['positionType']
                item['workYear'] = result['workYear']
                item['education'] = result['education']
                item['jobNature'] = result['jobNature']
                item['createTime'] = result['createTime']
                item['companyShortName'] = result['companyShortName']
                item['positionFirstType'] = result['positionFirstType']
                item['positionId'] = result['positionId']
                item['salary'] = result['salary']
                item['city'] = result['city']
                item['positionAdvantage'] = result['positionAdvantage']
                item['companyName'] = result['companyName']
                item['companyLogo'] = result['companyLogo']
                item['industryField'] = result['industryField']
                item['financeStage'] = result['financeStage']
                item['companyLabelList'] = result['companyLabelList']
                item['leaderName'] = result['leaderName']
                item['companySize'] = result['companySize']
                item['deliverCount'] = result['deliverCount']
                item['score'] = result['score']
                item['adjustScore'] = result['adjustScore']
                item['relScore'] = result['relScore']
                item['formatCreateTime'] = result['formatCreateTime']
                item['randomScore'] = result['randomScore']
                item['countAdjusted'] = result['countAdjusted']
                item['calcScore'] = result['calcScore']
                item['orderBy'] = result['orderBy']
                item['showOrder'] = result['showOrder']
                item['haveDeliver'] = result['haveDeliver']
                item['adWord'] = result['adWord']
                item['createTimeSort'] = result['createTimeSort']
                item['positonTypesMap'] = result['positonTypesMap']
                item['hrScore'] = result['hrScore']
                item['flowScore'] = result['flowScore']
                item['showCount'] = result['showCount']
                item['pvScore'] = result['pvScore']
                item['plus'] = result['plus']
                item['imstate'] = result['imstate']
                item['totalCount'] = result['totalCount']
                item['searchScore'] = result['searchScore']
                yield item

                companyId = result['companyId']
                company_item = CompanyItem()
                company_item['companyId'] = companyId
                company_item['companyShortName'] = result['companyShortName']
                company_item['companyName'] = result['companyName']
                company_item['financeStage'] = result['financeStage']
                company_item['companySize'] = result['companySize']
                yield self.get_company_request(company_item)

            request = self.get_request_by_pg(int(pg_no) + 1)
            yield request

    def parse_company(self, response):
        xp = '//*[@id="interview_container"]/div[3]/div[1]/div/span[2]'
        company_item = response.request.meta['company_item']
        matchs = response.xpath(xp)
        if matchs:
            txt = matchs[0].extract()
            cmp = '<span class="score">(.+)</span>'
            m = re.match(cmp, txt)
            if m:
                score = m.group(1)
                company_item['score'] = score
                for line in response.body.splitlines():
                    s1 = r"""<script id="companyInfoData" type="text/html">"""
                    endidx = 0 - len("</script>")
                    if s1 in line:
                        start = len(s1)
                        # company.json
                        interviewExperiencesData = line.strip()[start:endidx]
                        r = json.loads(interviewExperiencesData)
                        location = r['location']
                        if location:
                            location = location[0]
                            company_item['lat'] = location['latitude']
                            company_item['lng'] = location['longitude']
                            company_item['briefPosition'] = location['briefPosition']
                            company_item['detailPosition'] = location['detailPosition']

                yield company_item
