# Generated by Django 3.1.3 on 2021-06-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulate_test', '0005_auto_20210607_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='option',
            field=models.IntegerField(verbose_name='选项'),
        ),
    ]
