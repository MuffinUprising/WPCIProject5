# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardsearch', '0005_remove_card_mechanics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_text',
        ),
        migrations.RemoveField(
            model_name='card',
            name='player_class',
        ),
    ]