# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 06:36


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_auto_20180317_0559"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="url",
        ),
        migrations.AlterField(
            model_name="post",
            name="posted_at",
            field=models.DateTimeField(verbose_name=b"posted at"),
        ),
    ]