# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20160510_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lat',
            field=models.FloatField(default=None, null=True, verbose_name=b'lat'),
        ),
        migrations.AlterField(
            model_name='company',
            name='lng',
            field=models.FloatField(default=None, null=True, verbose_name=b'lng'),
        ),
    ]
