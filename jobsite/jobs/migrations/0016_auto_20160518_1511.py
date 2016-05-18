# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_company_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='briefPosition',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'briefPosition', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='detailPosition',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'detailPosition', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(default=b'unknow', max_length=100, verbose_name=b'status', choices=[(b'poor', b'poor'), (b'unknow', b'unknow'), (b'excellent', b'excellent')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='positionType',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
    ]
