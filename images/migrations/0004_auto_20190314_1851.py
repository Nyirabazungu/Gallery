# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20190314_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['category']},
        ),
        migrations.AddField(
            model_name='images',
            name='images_images',
            field=models.ImageField(default=5, upload_to='images/'),
            preserve_default=False,
        ),
    ]