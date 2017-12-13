# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('working_ind', models.BooleanField()),
                ('employee_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personnel.Personnel')),
            ],
        ),
    ]
