# Generated by Django 2.0.1 on 2020-01-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20200127_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='not_found_path',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='not_found_path_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='not_found_path_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]