# Generated by Django 2.2 on 2019-05-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190510_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutab',
            name='menutab_adres',
            field=models.TextField(null=True),
        ),
    ]
