# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_auto_20171213_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='employee_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.Personnel'),
        ),
    ]