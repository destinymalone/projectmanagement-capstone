# Generated by Django 3.0.4 on 2020-04-03 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userboardlist',
            name='header',
        ),
    ]
