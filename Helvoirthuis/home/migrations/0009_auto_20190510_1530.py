# Generated by Django 2.2 on 2019-05-10 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_menutabs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='menutabs',
            new_name='menutab',
        ),
        migrations.RenameField(
            model_name='menutab',
            old_name='menutabs_title',
            new_name='menutab_title',
        ),
    ]
