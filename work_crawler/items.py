# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    companyId = scrapy.Field()
    companyShortName = scrapy.Field()
    companyName = scrapy.Field()
    financeStage = scrapy.Field()
    companySize = scrapy.Field()

    address = scrapy.Field()
    briefPosition = scrapy.Field()
    detailPosition = scrapy.Field()
    score = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()


class JobItem(scrapy.Item):
    companyId = scrapy.Field()  # 115639
    positionName = scrapy.Field()  # "Python"
    positionType = scrapy.Field()  # "后端开发"
    workYear = scrapy.Field()  # "不限"
    education = scrapy.Field()  # "本科"
    jobNature = scrapy.Field()  # "全职"
    createTime = scrapy.Field()  # "2016-04-27 17:17:50"
    companyShortName = scrapy.Field()  # "北京凯博创盈科技发展有限公司"
    positionFirstType = scrapy.Field()  # "技术"
    positionId = scrapy.Field()  # 1580725
    salary = scrapy.Field()  # "8k-16k"
    city = scrapy.Field()  # "北京"
    positionAdvantage = scrapy.Field()  # "晋升空间"
    companyName = scrapy.Field()  # "北京凯博创盈科技发展有限公司"
    companyLogo = scrapy.Field()  # "i/image/M00/06/EB/Cgp3O1bNXnOAb0JEAAAHYPkPBTc687.png"
    industryField = scrapy.Field()  # "移动互联网 · 数据服务"
    financeStage = scrapy.Field()  # "初创型(未融资)"
    companyLabelList = scrapy.Field()  # []
    leaderName = scrapy.Field()  # "暂没有填写"
    companySize = scrapy.Field()  # "15-50人"
    deliverCount = scrapy.Field()  # 3
    score = scrapy.Field()  # 1208
    adjustScore = scrapy.Field()  # 0
    relScore = scrapy.Field()  # 1000
    formatCreateTime = scrapy.Field()  # "1天前发布"
    randomScore = scrapy.Field()  # 0
    countAdjusted = scrapy.Field()  # false
    calcScore = scrapy.Field()  # false
    orderBy = scrapy.Field()  # 60
    showOrder = scrapy.Field()  # 0
    haveDeliver = scrapy.Field()  # false
    adWord = scrapy.Field()  # 0
    createTimeSort = scrapy.Field()  # 1461748670000
    positonTypesMap = scrapy.Field()  # null
    hrScore = scrapy.Field()  # 62
    flowScore = scrapy.Field()  # 86
    showCount = scrapy.Field()  # 238
    pvScore = scrapy.Field()  # 48.04361074035268
    plus = scrapy.Field()  # "否"
    imstate = scrapy.Field()  # "disabled"
    totalCount = scrapy.Field()  # 0
    searchScore = scrapy.Field()  # 0.