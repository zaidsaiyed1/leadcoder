# Generated by Django 5.1.1 on 2024-10-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_quiz_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='levelofq',
            field=models.CharField(max_length=20, null=True),
        ),
    ]