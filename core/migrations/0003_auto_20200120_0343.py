# Generated by Django 2.0.1 on 2020-01-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='footer_home_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='settings',
            name='footer_joinus_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='settings',
            name='footer_manifesto_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='settings',
            name='footer_whatwedo_url',
            field=models.CharField(max_length=255),
        ),
    ]