# Generated by Django 2.0.1 on 2020-01-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200120_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.FileField(default=1, upload_to='partners'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partners',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
