# Generated by Django 2.2.9 on 2021-11-05 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='Projeto',
            new_name='Projeto_id',
        ),
    ]