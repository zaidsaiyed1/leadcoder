# Generated by Django 5.0.6 on 2024-08-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
