# Generated by Django 3.2.19 on 2023-08-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='point',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
