# Generated by Django 3.1.5 on 2021-02-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20210202_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='git_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='repo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]