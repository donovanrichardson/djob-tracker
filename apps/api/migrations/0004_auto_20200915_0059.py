# Generated by Django 3.1.1 on 2020-09-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200913_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='keywords',
            field=models.CharField(max_length=255, null=True),
        ),
    ]