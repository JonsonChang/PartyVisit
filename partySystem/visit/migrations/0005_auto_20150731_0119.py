# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_auto_20150731_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='password',
            field=models.CharField(default=b'123456789', max_length=255, verbose_name=b'\xe5\xaf\x86\xe7\xa2\xbc'),
        ),
    ]
