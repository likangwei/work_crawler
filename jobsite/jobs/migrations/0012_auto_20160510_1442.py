# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20160510_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cid',
            field=models.IntegerField(unique=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8ID'),
        ),
    ]
