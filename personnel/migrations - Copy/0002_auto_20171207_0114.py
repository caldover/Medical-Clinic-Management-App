# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physician',
            name='id',
        ),
        migrations.AlterField(
            model_name='physician',
            name='employee_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personnel.Personnel'),
        ),
    ]
