# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_job_crawl_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='companyName',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='companyShortName',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='companySize',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='financeStage',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='lat',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='lng',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AddField(
            model_name='company',
            name='score',
            field=models.FloatField(default=0, verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe5\xbe\x97\xe5\x88\x86'),
        ),
    ]
