# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0003_auto_20150731_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='introducer',
            field=models.IntegerField(default=0, null=True, verbose_name=b'\xe4\xbb\x8b\xe7\xb4\xb9\xe4\xba\xba'),
        ),
    ]
