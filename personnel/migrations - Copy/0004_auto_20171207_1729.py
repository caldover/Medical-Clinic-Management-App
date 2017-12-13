# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_auto_20171207_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surgeon',
            name='id',
        ),
        migrations.AlterField(
            model_name='physician',
            name='employee_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personnel.Personnel'),
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='employee_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personnel.Personnel'),
        ),
    ]