# Generated by Django 3.1.1 on 2020-09-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default='example.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]
