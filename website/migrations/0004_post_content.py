# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 14:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160613_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Content',
            field=models.TextField(default=datetime.datetime(2016, 6, 13, 14, 50, 12, 700150, tzinfo=utc)),
            preserve_default=False,
        ),
    ]