# Generated by Django 2.0.1 on 2020-01-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_joinus'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='joinus_title',
            field=models.CharField(default='Join us', max_length=255),
        ),
    ]
