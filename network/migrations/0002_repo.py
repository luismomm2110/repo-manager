# Generated by Django 3.1.5 on 2021-01-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=128)),
                ('link', models.CharField(max_length=128)),
            ],
        ),
    ]
