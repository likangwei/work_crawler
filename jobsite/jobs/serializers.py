#coding=utf8

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Job
from models import Company


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
