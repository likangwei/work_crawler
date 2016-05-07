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
                    "industryField"]
    list_filter = ["salary", "workYear"]
    list_per_page = 100
    actions = []


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)