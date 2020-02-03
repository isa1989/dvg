# Generated by Django 2.0.1 on 2020-01-21 17:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_settings_joinus_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Work shop',
                'verbose_name_plural': 'Work shop',
            },
        ),
    ]