# Generated by Django 3.1.7 on 2021-03-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210311_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='image',
            field=models.ImageField(null=True, upload_to='models/personaje/images'),
        ),
    ]
