# Generated by Django 2.2 on 2019-06-15 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='users',
        ),
    ]