# Generated by Django 2.0.1 on 2020-01-20 05:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200120_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='home_title_plane',
            field=ckeditor.fields.RichTextField(default='DVG is a common platform where product owners, agile leaders, designers and engineers collaborate to invent, design and develop new products and technologies or upgrade existing digital platforms.'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='home_we_garner',
            field=ckeditor.fields.RichTextField(default='We garner testable ideas and deliver results based on data and expertise. We lead with agility and'),
        ),
    ]
