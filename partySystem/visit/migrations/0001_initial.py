# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('vil', models.CharField(max_length=255)),
                ('nei', models.CharField(max_length=255)),
                ('rd', models.CharField(max_length=255)),
                ('seg', models.CharField(max_length=255)),
                ('lane', models.CharField(max_length=255)),
                ('aller', models.CharField(max_length=255)),
                ('num', models.CharField(max_length=255)),
                ('f', models.CharField(max_length=255)),
            ],
        ),
    ]
