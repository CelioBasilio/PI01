# Generated by Django 2.2.24 on 2021-11-28 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211128_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='empresa',
        ),
    ]