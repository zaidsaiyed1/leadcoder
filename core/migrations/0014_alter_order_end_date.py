# Generated by Django 5.0.6 on 2024-08-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_order_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
