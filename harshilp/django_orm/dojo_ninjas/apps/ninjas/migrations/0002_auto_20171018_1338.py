# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-18 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dojos',
            new_name='Dojo',
        ),
        migrations.RenameModel(
            old_name='Ninjas',
            new_name='Ninja',
        ),
    ]
