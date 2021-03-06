# Generated by Django 2.0.1 on 2020-01-21 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200121_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
                ('order', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModalMenu')),
            ],
            options={
                'verbose_name': 'Modal Menyu',
                'verbose_name_plural': 'Modal Menyular',
                'ordering': ('order',),
            },
        ),
    ]
