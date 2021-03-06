# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-18 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.CharField(choices=[('\u4e0a\u5348', '\u4e0a\u5348'), ('\u4e0b\u5348', '\u4e0b\u5348')], max_length=100, null=True)),
                ('place', models.CharField(max_length=150, null=True)),
                ('speaker', models.CharField(max_length=150, null=True)),
                ('url_id', models.CharField(blank=True, max_length=20, null=True)),
                ('download_date', models.DateTimeField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
