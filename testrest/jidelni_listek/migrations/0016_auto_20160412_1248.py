# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jidelni_listek', '0015_auto_20160412_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='plist',
            field=models.ForeignKey(related_name='+', default=b'', blank=True, to='jidelni_listek.Product', null=True, verbose_name=b'Doporu\xc4\x8den\xc3\xa9 pivo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 10, 48, 14, 616974, tzinfo=utc), verbose_name=b'Platnost od'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vlist',
            field=models.ForeignKey(related_name='+', default=b'', blank=True, to='jidelni_listek.Product', null=True, verbose_name=b'Doporu\xc4\x8den\xc3\xa9 v\xc3\xadno'),
        ),
    ]
