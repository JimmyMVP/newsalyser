# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='top_taxonomy',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
