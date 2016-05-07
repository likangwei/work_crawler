# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20160507_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='companyLabelList',
        ),
    ]
