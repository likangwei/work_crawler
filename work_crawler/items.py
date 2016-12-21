# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from jobs.models import Job
from jobs.models import Company


class CompanyItem(DjangoItem):
    django_model = Company


class JobItem(DjangoItem):
    django_model = Job
