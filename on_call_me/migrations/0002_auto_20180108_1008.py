# Generated by Django 2.0.1 on 2018-01-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('on_call_me', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oncallperiod',
            old_name='hours',
            new_name='days',
        ),
    ]