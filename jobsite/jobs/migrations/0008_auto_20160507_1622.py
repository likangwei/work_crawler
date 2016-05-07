# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20160507_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='positionId',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'id', db_index=True),
        ),
    ]
