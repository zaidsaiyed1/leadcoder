# Generated by Django 5.1.1 on 2024-11-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_is_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
