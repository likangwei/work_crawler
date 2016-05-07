# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_company_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='formatCreateTime',
        ),
        migrations.AlterField(
            model_name='job',
            name='adWord',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'adWord'),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82'),
        ),
        migrations.AlterField(
            model_name='job',
            name='companyLabelList',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8label'),
        ),
        migrations.AlterField(
            model_name='job',
            name='companyName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='job',
            name='companyShortName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='job',
            name='companySize',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AlterField(
            model_name='job',
            name='createTime',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='job',
            name='createTimeSort',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
        ),
        migrations.AlterField(
            model_name='job',
            name='education',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\xad\xa6\xe5\x8e\x86'),
        ),
        migrations.AlterField(
            model_name='job',
            name='financeStage',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe7\x8e\xb0\xe7\x8a\xb6'),
        ),
        migrations.AlterField(
            model_name='job',
            name='haveDeliver',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xb7\xb2\xe6\x8a\x95\xe9\x80\x92'),
        ),
        migrations.AlterField(
            model_name='job',
            name='hrScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'HR\xe5\xbe\x97\xe5\x88\x86'),
        ),
        migrations.AlterField(
            model_name='job',
            name='industryField',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x96\xb9\xe5\x90\x91'),
        ),
        migrations.AlterField(
            model_name='job',
            name='leaderName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'leader'),
        ),
        migrations.AlterField(
            model_name='job',
            name='orderBy',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'60'),
        ),
        migrations.AlterField(
            model_name='job',
            name='positionId',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'id'),
        ),
        migrations.AlterField(
            model_name='job',
            name='positionName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='job',
            name='positionType',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe8\x96\xaa\xe8\xb5\x84\xe8\x8c\x83\xe5\x9b\xb4'),
        ),
        migrations.AlterField(
            model_name='job',
            name='showCount',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='job',
            name='showOrder',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'0'),
        ),
        migrations.AlterField(
            model_name='job',
            name='workYear',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xb9\xb4\xe9\x99\x90'),
        ),
    ]
