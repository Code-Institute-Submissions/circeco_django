# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='image',
            field=models.BinaryField(null=True),
        ),
    ]
