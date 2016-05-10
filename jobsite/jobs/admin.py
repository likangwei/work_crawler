#coding=utf8
from django.contrib import admin
from models import Job
from models import Company
from django.http import HttpResponse
from django.shortcuts import render


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name']



class JobAdmin(admin.ModelAdmin):
    # fields = ('nickname',)
    list_display = ["positionName",
                    "workYear",
                    "companyName",
                    "salary",
                    "city",
                    "industryField",
                    "crawl_fmttime",
                    ]

    def crawl_fmttime(self, obj):
        return obj.crawl_date.strftime('%Y-%m-%d')

    crawl_fmttime.admin_order_field = "crawl_date"

    list_filter = ["salary", "workYear", "crawl_date"]
    list_per_page = 100
    actions = []


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)