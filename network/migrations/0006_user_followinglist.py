# Generated by Django 3.1.1 on 2020-10-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20201004_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followingList',
            field=models.TextField(default=''),
        ),
    ]
