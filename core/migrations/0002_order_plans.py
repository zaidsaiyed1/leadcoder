# Generated by Django 5.0.6 on 2024-08-13 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='plans',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.plans'),
            preserve_default=False,
        ),
    ]
