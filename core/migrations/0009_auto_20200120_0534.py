# Generated by Django 2.0.1 on 2020-01-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200120_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='home_we_garner',
            field=models.TextField(),
        ),
    ]