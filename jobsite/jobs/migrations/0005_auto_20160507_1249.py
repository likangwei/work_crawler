# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20160507_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='plus',
        ),
        migrations.RemoveField(
            model_name='job',
            name='searchScore',
        ),
        migrations.RemoveField(
            model_name='job',
            name='totalCount',
        ),
    ]
