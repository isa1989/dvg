# Generated by Django 2.0.1 on 2020-01-27 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20200127_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='home_page_title',
            field=models.CharField(default='Home', max_length=255),
        ),
        migrations.AddField(
            model_name='settings',
            name='home_page_title_az',
            field=models.CharField(default='Home', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='home_page_title_en',
            field=models.CharField(default='Home', max_length=255, null=True),
        ),
    ]
