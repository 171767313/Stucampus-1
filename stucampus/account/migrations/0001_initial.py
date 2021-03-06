# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-18 14:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('true_name', models.CharField(max_length=20)),
                ('college', models.CharField(blank=True, choices=[(b'SF', b'\xe5\xb8\x88\xe8\x8c\x83\xe5\xad\xa6\xe9\x99\xa2'), (b'WX', b'\xe6\x96\x87\xe5\xad\xa6\xe9\x99\xa2'), (b'WGY', b'\xe5\xa4\x96\xe5\x9b\xbd\xe8\xaf\xad\xe5\xad\xa6\xe9\x99\xa2'), (b'CB', b'\xe4\xbc\xa0\xe6\x92\xad\xe5\xad\xa6\xe9\x99\xa2'), (b'JJ', b'\xe7\xbb\x8f\xe6\xb5\x8e\xe5\xad\xa6\xe9\x99\xa2'), (b'GL', b'\xe7\xae\xa1\xe7\x90\x86\xe5\xad\xa6\xe9\x99\xa2'), (b'FX', b'\xe6\xb3\x95\xe5\xad\xa6\xe9\x99\xa2'), (b'YS', b'\xe8\x89\xba\xe6\x9c\xaf\xe8\xae\xbe\xe8\xae\xa1\xe5\xad\xa6\xe9\x99\xa2'), (b'SK', b'\xe7\xa4\xbe\xe4\xbc\x9a\xe7\xa7\x91\xe5\xad\xa6\xe5\xad\xa6\xe9\x99\xa2'), (b'SX', b'\xe6\x95\xb0\xe5\xad\xa6\xe4\xb8\x8e\xe8\xae\xa1\xe7\xae\x97\xe7\xa7\x91\xe5\xad\xa6\xe5\xad\xa6\xe9\x99\xa2'), (b'WL', b'\xe7\x89\xa9\xe7\x90\x86\xe7\xa7\x91\xe5\xad\xa6\xe4\xb8\x8e\xe6\x8a\x80\xe6\x9c\xaf\xe5\xad\xa6\xe9\x99\xa2'), (b'HG', b'\xe5\x8c\x96\xe5\xad\xa6\xe4\xb8\x8e\xe5\x8c\x96\xe5\xb7\xa5\xe5\xad\xa6\xe9\x99\xa2'), (b'CL', b'\xe6\x9d\x90\xe6\x96\x99\xe5\xad\xa6\xe9\x99\xa2'), (b'XX', b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xad\xa6\xe9\x99\xa2'), (b'JR', b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe4\xb8\x8e\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xad\xa6\xe9\x99\xa2'), (b'JG', b'\xe5\xbb\xba\xe7\xad\x91\xe4\xb8\x8e\xe5\x9f\x8e\xe5\xb8\x82\xe8\xa7\x84\xe5\x88\x92\xe5\xad\xa6\xe9\x99\xa2'), (b'TM', b'\xe5\x9c\x9f\xe6\x9c\xa8\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xad\xa6\xe9\x99\xa2'), (b'DZ', b'\xe7\x94\xb5\xe5\xad\x90\xe7\xa7\x91\xe5\xad\xa6\xe4\xb8\x8e\xe6\x8a\x80\xe6\x9c\xaf\xe5\xad\xa6\xe9\x99\xa2'), (b'JD', b'\xe6\x9c\xba\xe7\x94\xb5\xe4\xb8\x8e\xe6\x8e\xa7\xe5\x88\xb6\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xad\xa6\xe9\x99\xa2'), (b'SK', b'\xe7\x94\x9f\xe5\x91\xbd\xe7\xa7\x91\xe5\xad\xa6\xe5\xad\xa6\xe9\x99\xa2'), (b'GD', b'\xe5\x85\x89\xe7\x94\xb5\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xad\xa6\xe9\x99\xa2'), (b'GEF', b'\xe9\xab\x98\xe5\xb0\x94\xe5\xa4\xab\xe5\xad\xa6\xe9\x99\xa2'), (b'YXY', b'\xe5\x8c\xbb\xe5\xad\xa6\xe9\x99\xa2'), (b'GJ', b'\xe5\x9b\xbd\xe9\x99\x85\xe4\xba\xa4\xe6\xb5\x81\xe5\xad\xa6\xe9\x99\xa2'), (b'JX', b'\xe7\xbb\xa7\xe7\xbb\xad\xe6\x95\x99\xe8\x82\xb2\xe5\xad\xa6\xe9\x99\xa2')], max_length=4, null=True)),
                ('screen_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[(b'M', '\u7537'), (b'F', '\u5973')], default=b'M', max_length=1)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('mobile_phone_number', models.CharField(max_length=11)),
                ('internal_phone_number', models.CharField(max_length=6)),
                ('job_id', models.CharField(max_length=10)),
                ('card_id', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('website_admin', '\u5b66\u5b50\u5929\u5730\u7f51\u7ad9\u7ba1\u7406\u5458'), ('student_manager', '\u5b66\u751f\u5e10\u53f7\u7ba1\u7406\u5458'), ('free_time_count', '\u7a7a\u95f2\u65f6\u95f4\u67e5\u770b\u7cfb\u7edf')),
            },
        ),
        migrations.CreateModel(
            name='UserActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('behavior', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
