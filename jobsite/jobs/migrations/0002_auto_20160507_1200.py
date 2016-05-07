# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='name',
        ),
        migrations.AddField(
            model_name='job',
            name='adWord',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0'),
        ),
        migrations.AddField(
            model_name='job',
            name='adjustScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0'),
        ),
        migrations.AddField(
            model_name='job',
            name='calcScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' false'),
        ),
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x8c\x97\xe4\xba\xac'),
        ),
        migrations.AddField(
            model_name='job',
            name='companyId',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'companyId'),
        ),
        migrations.AddField(
            model_name='job',
            name='companyLabelList',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'[]'),
        ),
        migrations.AddField(
            model_name='job',
            name='companyName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x8c\x97\xe4\xba\xac\xe5\x87\xaf\xe5\x8d\x9a\xe5\x88\x9b\xe7\x9b\x88\xe7\xa7\x91\xe6\x8a\x80\xe5\x8f\x91\xe5\xb1\x95\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8'),
        ),
        migrations.AddField(
            model_name='job',
            name='companyShortName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x8c\x97\xe4\xba\xac\xe5\x87\xaf\xe5\x8d\x9a\xe5\x88\x9b\xe7\x9b\x88\xe7\xa7\x91\xe6\x8a\x80\xe5\x8f\x91\xe5\xb1\x95\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8'),
        ),
        migrations.AddField(
            model_name='job',
            name='companySize',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'15-50\xe4\xba\xba'),
        ),
        migrations.AddField(
            model_name='job',
            name='countAdjusted',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' false'),
        ),
        migrations.AddField(
            model_name='job',
            name='createTime',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'2016-04-27 17:17:50'),
        ),
        migrations.AddField(
            model_name='job',
            name='createTimeSort',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 1461748670000'),
        ),
        migrations.AddField(
            model_name='job',
            name='deliverCount',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 3'),
        ),
        migrations.AddField(
            model_name='job',
            name='education',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x9c\xac\xe7\xa7\x91'),
        ),
        migrations.AddField(
            model_name='job',
            name='financeStage',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x88\x9d\xe5\x88\x9b\xe5\x9e\x8b(\xe6\x9c\xaa\xe8\x9e\x8d\xe8\xb5\x84)'),
        ),
        migrations.AddField(
            model_name='job',
            name='flowScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 86'),
        ),
        migrations.AddField(
            model_name='job',
            name='formatCreateTime',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'1\xe5\xa4\xa9\xe5\x89\x8d\xe5\x8f\x91\xe5\xb8\x83'),
        ),
        migrations.AddField(
            model_name='job',
            name='haveDeliver',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' false'),
        ),
        migrations.AddField(
            model_name='job',
            name='hrScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 62'),
        ),
        migrations.AddField(
            model_name='job',
            name='imstate',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'disabled'),
        ),
        migrations.AddField(
            model_name='job',
            name='industryField',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe7\xa7\xbb\xe5\x8a\xa8\xe4\xba\x92\xe8\x81\x94\xe7\xbd\x91 \xc2\xb7 \xe6\x95\xb0\xe6\x8d\xae\xe6\x9c\x8d\xe5\x8a\xa1'),
        ),
        migrations.AddField(
            model_name='job',
            name='jobNature',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xa8\xe8\x81\x8c'),
        ),
        migrations.AddField(
            model_name='job',
            name='leaderName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x9a\x82\xe6\xb2\xa1\xe6\x9c\x89\xe5\xa1\xab\xe5\x86\x99'),
        ),
        migrations.AddField(
            model_name='job',
            name='orderBy',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 60'),
        ),
        migrations.AddField(
            model_name='job',
            name='plus',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x90\xa6'),
        ),
        migrations.AddField(
            model_name='job',
            name='positionAdvantage',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x99\x8b\xe5\x8d\x87\xe7\xa9\xba\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='job',
            name='positionFirstType',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x8a\x80\xe6\x9c\xaf'),
        ),
        migrations.AddField(
            model_name='job',
            name='positionId',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'1580725'),
        ),
        migrations.AddField(
            model_name='job',
            name='positionName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'Python'),
        ),
        migrations.AddField(
            model_name='job',
            name='positionType',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x90\x8e\xe7\xab\xaf\xe5\xbc\x80\xe5\x8f\x91'),
        ),
        migrations.AddField(
            model_name='job',
            name='positonTypesMap',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' null'),
        ),
        migrations.AddField(
            model_name='job',
            name='pvScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 48.04361074035268'),
        ),
        migrations.AddField(
            model_name='job',
            name='randomScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0'),
        ),
        migrations.AddField(
            model_name='job',
            name='relScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 1000'),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'8k-16k'),
        ),
        migrations.AddField(
            model_name='job',
            name='score',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 1208'),
        ),
        migrations.AddField(
            model_name='job',
            name='searchScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0.'),
        ),
        migrations.AddField(
            model_name='job',
            name='showCount',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 238'),
        ),
        migrations.AddField(
            model_name='job',
            name='showOrder',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0'),
        ),
        migrations.AddField(
            model_name='job',
            name='totalCount',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' 0'),
        ),
        migrations.AddField(
            model_name='job',
            name='workYear',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe4\xb8\x8d\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
