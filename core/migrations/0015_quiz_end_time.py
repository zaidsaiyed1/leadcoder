# Generated by Django 5.0.6 on 2024-09-09 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_order_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 9, 9, 18, 13, 19, 77664)),
            preserve_default=False,
        ),
    ]
