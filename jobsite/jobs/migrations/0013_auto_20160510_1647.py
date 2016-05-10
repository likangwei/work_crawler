# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20160510_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='briefPosition',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'briefPosition'),
        ),
        migrations.AddField(
            model_name='company',
            name='detailPosition',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'detailPosition'),
        ),
    ]
