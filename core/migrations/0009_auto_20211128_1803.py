# Generated by Django 2.2.24 on 2021-11-28 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211128_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='empresa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to='core.Empresa'),
        ),
    ]
