# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store', models.CharField(max_length=255, verbose_name=b'\xe5\xba\x97\xe5\xae\xb6\xe5\x90\x8d', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name=b'\xe7\xb8\xa3/\xe5\xb8\x82')),
                ('area', models.CharField(max_length=255, verbose_name=b'\xe5\x8d\x80')),
                ('vil', models.CharField(max_length=255, verbose_name=b'\xe9\x87\x8c/\xe6\x9d\x91', blank=True)),
                ('nei', models.CharField(max_length=255, verbose_name=b'\xe9\x84\xb0', blank=True)),
                ('rd', models.CharField(max_length=255, verbose_name=b'\xe8\xb7\xaf/\xe8\xa1\x97', blank=True)),
                ('seg', models.CharField(max_length=255, verbose_name=b'\xe6\xae\xb5', blank=True)),
                ('lane', models.CharField(max_length=255, verbose_name=b'\xe5\xb7\xb7', blank=True)),
                ('aller', models.CharField(max_length=255, verbose_name=b'\xe5\xbc\x84', blank=True)),
                ('num', models.CharField(max_length=255, verbose_name=b'\xe8\x99\x9f', blank=True)),
                ('f', models.CharField(max_length=255, verbose_name=b'\xe6\xa8\x93', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x8b\x9c\xe8\xa8\xaa\xe6\x97\xa5\xe6\x9c\x9f')),
                ('record', models.TextField(verbose_name=b'\xe8\xa8\x98\xe9\x8c\x84')),
                ('address', models.ForeignKey(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', to='visit.address')),
            ],
        ),
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_del', models.BooleanField(default=False, verbose_name=b'\xe5\x81\x9c\xe7\x94\xa8')),
                ('auth', models.IntegerField(default=0, verbose_name=b'\xe6\xac\x8a\xe9\x99\x90', choices=[(0, b'\xe6\xb0\x91\xe7\x9c\xbe'), (1, b'\xe7\xbe\xa9\xe5\xb7\xa5'), (2, b'\xe9\x9a\x8a\xe9\x95\xb7'), (99, b'\xe7\xae\xa1\xe7\x90\x86\xe8\x80\x85')])),
                ('state', models.IntegerField(default=0, verbose_name=b'\xe8\xaa\x8d\xe5\x90\x8c\xe7\x8b\x80\xe6\x85\x8b', choices=[(0, b'\xe7\x84\xa1\xe7\x8b\x80\xe6\x85\x8b'), (1, b'\xe6\x8b\x92\xe6\xb1\xba'), (2, b'\xe8\xaa\x8d\xe5\x90\x8c'), (9, b'\xe5\xb7\xb2\xe5\x85\xa5\xe9\xbb\xa8')])),
                ('password', models.CharField(default=b'123456789', max_length=255, verbose_name=b'\xe5\xaf\x86\xe7\xa2\xbc')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('user_id', models.CharField(unique=True, max_length=10, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xad\x89\xe5\xad\x97\xe8\x99\x9f', blank=True)),
                ('sex', models.IntegerField(default=0, verbose_name=b'\xe6\x80\xa7\xe5\x88\xa5', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')])),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True)),
                ('introducer', models.CharField(default=b'', max_length=255, verbose_name=b'\xe4\xbb\x8b\xe7\xb4\xb9\xe4\xba\xba')),
                ('tel_office', models.CharField(max_length=255, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe9\x9b\xbb\xe8\xa9\xb1', blank=True)),
                ('tel_home', models.CharField(max_length=255, verbose_name=b'\xe4\xbd\x8f\xe5\xae\xb6\xe9\x9b\xbb\xe8\xa9\xb1', blank=True)),
                ('tel_mobile', models.CharField(max_length=255, verbose_name=b'\xe6\x89\x8b\xe6\xa9\x9f', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name=b'Email', blank=True)),
                ('edu', models.IntegerField(default=0, verbose_name=b'\xe5\xad\xb8\xe6\xad\xb7', choices=[(1, b'\xe5\x9c\x8b\xe5\xb0\x8f'), (2, b'\xe5\x9c\x8b\xe4\xb8\xad'), (3, b'\xe9\xab\x98\xe4\xb8\xad/\xe8\x81\xb7'), (4, b'\xe5\xb0\x88\xe7\xa7\x91'), (5, b'\xe5\xad\xb8\xe5\xa3\xab'), (6, b'\xe7\xa2\xa9\xe5\xa3\xab'), (7, b'\xe5\x8d\x9a\xe5\xa3\xab')])),
                ('school_status', models.IntegerField(default=0, verbose_name=b'\xe5\xb0\xb1\xe8\xae\x80\xe7\x95\xa2\xe6\xa5\xad', choices=[(0, b'\xe7\x95\xa2\xe6\xa5\xad'), (1, b'\xe5\xb0\xb1\xe8\xae\x80')])),
                ('school', models.CharField(max_length=255, verbose_name=b'\xe5\xad\xb8\xe6\xa0\xa1', blank=True)),
                ('major', models.CharField(max_length=255, verbose_name=b'\xe7\xa7\x91\xe7\xb3\xbb', blank=True)),
                ('company', models.CharField(max_length=255, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa8\xb1', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe8\x81\xb7\xe7\xa8\xb1', blank=True)),
                ('religion', models.IntegerField(default=0, verbose_name=b'\xe5\xae\x97\xe6\x95\x99\xe4\xbf\xa1\xe4\xbb\xb0', choices=[(1, b'\xe4\xbd\x9b\xe6\x95\x99'), (2, b'\xe5\x9b\x9e\xe6\x95\x99'), (3, b'\xe9\x81\x93\xe6\x95\x99'), (4, b'\xe5\xa4\xa9\xe4\xb8\xbb\xe6\x95\x99'), (5, b'\xe5\x9f\xba\xe7\x9d\xa3\xe6\x95\x99'), (6, b'\xe4\xb8\x80\xe8\xb2\xab\xe9\x81\x93'), (7, b'\xe7\x84\xa1'), (8, b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('is_other_political_party', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x83\xe5\x8a\xa0\xe9\x81\x8e\xe5\x85\xb6\xe4\xbb\x96\xe6\x94\xbf\xe9\xbb\xa8', choices=[(0, b'\xe6\x9c\xaa\xe6\x9b\xbe\xe5\x8a\xa0\xe5\x85\xa5\xe5\x85\xb6\xe4\xbb\x96\xe6\x94\xbf\xe9\xbb\xa8'), (1, b'\xe5\xa2\x9e\xe5\x8a\xa0\xe5\x85\xa5')])),
                ('political_party', models.CharField(max_length=255, verbose_name=b'\xe6\x94\xbf\xe9\xbb\xa8\xe5\x90\x8d\xe7\xa8\xb1', blank=True)),
                ('address', models.ForeignKey(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', to='visit.address')),
            ],
        ),
    ]
