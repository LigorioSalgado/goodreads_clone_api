# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-06 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0005_auto_20170505_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Books.Book'),
        ),
    ]