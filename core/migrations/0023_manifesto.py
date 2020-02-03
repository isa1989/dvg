# Generated by Django 2.0.1 on 2020-01-21 17:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_modalmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_bold', models.CharField(max_length=300)),
                ('title_plane', ckeditor.fields.RichTextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Manifesto',
                'verbose_name_plural': 'Manifesto',
            },
        ),
    ]