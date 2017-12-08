# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_auto_20171207_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='id',
        ),
        migrations.AlterField(
            model_name='nurse',
            name='employee_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personnel.Personnel'),
        ),
    ]
