# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jidelni_listek', '0012_auto_20160412_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 10, 47, 14, 227811, tzinfo=utc), verbose_name=b'Platnost od'),
        ),
    ]
