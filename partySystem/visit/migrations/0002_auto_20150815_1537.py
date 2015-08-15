# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='introducer',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'\xe4\xbb\x8b\xe7\xb4\xb9\xe4\xba\xba', blank=True),
        ),
    ]
