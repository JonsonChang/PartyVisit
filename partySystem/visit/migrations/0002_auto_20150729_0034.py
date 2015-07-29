# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='store',
            field=models.CharField(max_length=255, verbose_name=b'store app'),
        ),
    ]
