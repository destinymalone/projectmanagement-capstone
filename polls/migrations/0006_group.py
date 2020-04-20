# Generated by Django 3.0.4 on 2020-04-19 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200417_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('order', models.IntegerField(default=100000)),
            ],
        ),
    ]
