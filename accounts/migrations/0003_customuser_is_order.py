# Generated by Django 5.0.6 on 2024-08-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_docsmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_order',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]