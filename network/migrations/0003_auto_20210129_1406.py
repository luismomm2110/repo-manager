# Generated by Django 3.1.5 on 2021-01-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_repo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repo',
            name='repo_id',
        ),
        migrations.AddField(
            model_name='repo',
            name='tag',
            field=models.CharField(default='NA', max_length=64),
        ),
        migrations.AlterField(
            model_name='repo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
