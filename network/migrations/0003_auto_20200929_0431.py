# Generated by Django 3.1.1 on 2020-09-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
