# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_job_companylabellist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='adjustScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'adjustScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='calcScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'calcScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='countAdjusted',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'countAdjusted'),
        ),
        migrations.AlterField(
            model_name='job',
            name='deliverCount',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'deliverCount'),
        ),
        migrations.AlterField(
            model_name='job',
            name='flowScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b' flowScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='haveDeliver',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'haveDeliver'),
        ),
        migrations.AlterField(
            model_name='job',
            name='imstate',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'imstate'),
        ),
        migrations.AlterField(
            model_name='job',
            name='orderBy',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'orderBy'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pvScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'pvScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='randomScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'randomScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='relScore',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'relScore'),
        ),
        migrations.AlterField(
            model_name='job',
            name='score',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'score'),
        ),
        migrations.AlterField(
            model_name='job',
            name='showOrder',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'showOrder'),
        ),
    ]
