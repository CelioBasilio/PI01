# Generated by Django 2.2.24 on 2021-11-28 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_projeto_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Empresa', to='core.Empresa'),
        ),
    ]
