# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160507_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cid',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8ID'),
            preserve_default=False,
        ),
    ]
