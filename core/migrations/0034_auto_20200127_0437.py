# Generated by Django 2.0.1 on 2020-01-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20200127_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='not_found_url',
            field=models.CharField(blank=True, default='Go To Homepage', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='not_found_url_az',
            field=models.CharField(blank=True, default='Go To Homepage', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='not_found_url_en',
            field=models.CharField(blank=True, default='Go To Homepage', max_length=300, null=True),
        ),
    ]
