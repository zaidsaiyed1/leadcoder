# Generated by Django 5.1.1 on 2024-11-14 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_number_customuser_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profilepic',
        ),
    ]