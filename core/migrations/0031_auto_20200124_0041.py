# Generated by Django 2.0.1 on 2020-01-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20200123_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='index_title_az',
            field=models.CharField(blank=True, default='What we do', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='index_title_en',
            field=models.CharField(blank=True, default='What we do', max_length=255, null=True),
        ),
    ]
