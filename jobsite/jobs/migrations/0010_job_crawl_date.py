# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20160507_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='crawl_date',
            field=models.DateField(default=datetime.datetime(2016, 5, 10, 3, 39, 36, 611412, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
