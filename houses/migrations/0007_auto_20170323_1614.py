# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20170323_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]