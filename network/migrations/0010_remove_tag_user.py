# Generated by Django 3.1.5 on 2021-02-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20210131_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
