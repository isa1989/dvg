# Generated by Django 2.0.1 on 2020-01-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20200127_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='logo_footer_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_footer_url_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_footer_url_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_header_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_header_url_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_header_url_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_home_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_home_url_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_home_url_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
