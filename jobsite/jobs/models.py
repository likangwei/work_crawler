#coding=utf8
from django.db import models

# Create your models here.


class Company(models.Model):
    STATUS_POOR = "poor"
    STATUS_EXCELLENT = "excellent"
    STATUS_UNKNOW = "unknow"

    STATUS_CHOICE = (
        (STATUS_POOR, STATUS_POOR),
        (STATUS_UNKNOW, STATUS_UNKNOW),
        (STATUS_EXCELLENT, STATUS_EXCELLENT),
    )
    cid = models.IntegerField(unique=True, verbose_name="公司ID")
    name = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    address = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    companyShortName = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    companyName = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    financeStage = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    companySize = models.CharField(max_length=100, default=None, null=True, verbose_name="公司名称")
    briefPosition = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name="briefPosition")
    detailPosition = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name="detailPosition")
    lat = models.FloatField(default=None, null=True, verbose_name="lat")
    lng = models.FloatField(default=None, null=True, verbose_name="lng")
    score = models.FloatField(default=0, verbose_name="综合得分")
    status = models.CharField(max_length=100, default=STATUS_UNKNOW, choices=STATUS_CHOICE, verbose_name="status")

    @property
    def detail(self):
        return '%s: 得分:%s, 工作:%d份' % (self.name, self.score, Job.objects.filter(companyId=self.cid)).count()


class Job(models.Model):
    companyId = models.CharField(max_length=255, default=None, null=True, verbose_name="companyId")
    positionName = models.CharField(max_length=255, default=None, null=True, verbose_name="职位")
    positionType = models.CharField(max_length=255, default=None, blank=True, null=True, verbose_name="职位类型")
    workYear = models.CharField(max_length=255, default=None, null=True, verbose_name="工作年限")
    education = models.CharField(max_length=255, default=None, null=True, verbose_name="学历")
    jobNature = models.CharField(max_length=255, default=None, null=True, verbose_name="全职")
    createTime = models.CharField(max_length=255, default=None, null=True, verbose_name="创建时间")
    companyShortName = models.CharField(max_length=255, default=None, null=True, verbose_name="公司名称")
    positionFirstType = models.CharField(max_length=255, blank=True, default=None, null=True, verbose_name="技术")
    positionId = models.CharField(max_length=255, default=None, null=True, unique=True, verbose_name="id")
    salary = models.CharField(max_length=255, default=None, null=True, verbose_name="薪资范围")
    city = models.CharField(max_length=255, default=None, null=True, verbose_name="城市")
    positionAdvantage = models.CharField(max_length=255, default=None, null=True, verbose_name="晋升空间")
    companyName = models.CharField(max_length=255, default=None, null=True, verbose_name="公司名称")
    industryField = models.CharField(max_length=255, default=None, null=True, verbose_name="公司方向")
    financeStage = models.CharField(max_length=255, default=None, null=True, verbose_name="公司现状")
    leaderName = models.CharField(max_length=255, default=None, null=True, verbose_name="leader")
    companySize = models.CharField(max_length=255, default=None, null=True, verbose_name="公司大小")
    deliverCount = models.CharField(max_length=255, default=None, null=True, verbose_name="deliverCount")
    score = models.CharField(max_length=255, default=None, null=True, verbose_name="score")
    adjustScore = models.CharField(max_length=255, default=None, null=True, verbose_name="adjustScore")
    relScore = models.CharField(max_length=255, default=None, null=True, verbose_name="relScore")
    randomScore = models.CharField(max_length=255, default=None, null=True, verbose_name="randomScore")
    countAdjusted = models.CharField(max_length=255, default=None, null=True, verbose_name="countAdjusted")
    calcScore = models.CharField(max_length=255, default=None, null=True, verbose_name="calcScore")
    orderBy = models.CharField(max_length=255, default=None, null=True, verbose_name="orderBy")
    showOrder = models.CharField(max_length=255, default=None, null=True, verbose_name="showOrder")
    haveDeliver = models.CharField(max_length=255, default=None, null=True, verbose_name="haveDeliver")
    adWord = models.CharField(max_length=255, default=None, null=True, verbose_name="adWord")
    createTimeSort = models.CharField(max_length=255, default=None, null=True, verbose_name="创建时间戳")
    positonTypesMap = models.CharField(max_length=255, default=None, null=True, verbose_name=" null")
    hrScore = models.CharField(max_length=255, default=None, null=True, verbose_name="HR得分")
    flowScore = models.CharField(max_length=255, default=None, null=True, verbose_name=" flowScore")
    showCount = models.CharField(max_length=255, default=None, null=True, verbose_name="展示次数")
    pvScore = models.CharField(max_length=255, default=None, null=True, verbose_name="pvScore")
    imstate = models.CharField(max_length=255, default=None, null=True, verbose_name="imstate")
    crawl_date = models.DateField(auto_now=True)
