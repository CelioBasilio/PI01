# Generated by Django 2.2.24 on 2021-11-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20211128_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
