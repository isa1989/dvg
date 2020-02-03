# Generated by Django 2.0.1 on 2020-01-21 17:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200121_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_bold', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Join us',
                'verbose_name_plural': 'Join us',
            },
        ),
    ]
