# Generated by Django 4.1.3 on 2022-11-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
