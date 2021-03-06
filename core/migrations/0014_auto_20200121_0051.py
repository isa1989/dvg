# Generated by Django 2.0.1 on 2020-01-21 00:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200120_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Strategic design & digital empowerment', max_length=300)),
                ('title_main', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'What we do',
                'verbose_name_plural': 'What we do',
            },
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Partner', 'verbose_name_plural': 'Partners'},
        ),
    ]
