# Generated by Django 2.2.24 on 2021-11-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211128_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empresa', to='core.Empresa'),
        ),
    ]
