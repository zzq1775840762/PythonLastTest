# Generated by Django 3.1.3 on 2021-06-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulate_test', '0002_auto_20210603_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='times',
            field=models.IntegerField(verbose_name='测试次数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='学号'),
        ),
    ]
