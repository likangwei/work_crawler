# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20160507_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='positionId',
            field=models.CharField(null=True, default=None, max_length=255, unique=True, verbose_name=b'id', db_index=True),
        ),
    ]
