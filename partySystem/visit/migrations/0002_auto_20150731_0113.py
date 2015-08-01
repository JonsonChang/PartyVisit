# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='user_id',
            field=models.CharField(max_length=10, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xad\x89\xe5\xad\x97\xe8\x99\x9f', blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='introducer',
            field=models.IntegerField(null=True, verbose_name=b'\xe4\xbb\x8b\xe7\xb4\xb9\xe4\xba\xba'),
        ),
    ]
