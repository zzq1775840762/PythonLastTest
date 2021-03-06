# Generated by Django 3.1.3 on 2021-06-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulate_test', '0004_auto_20210607_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='得分')),
                ('result', models.IntegerField(verbose_name='类别')),
            ],
            options={
                'verbose_name': '答题结果',
                'verbose_name_plural': '答题结果',
                'db_table': 'Result',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('option', models.CharField(max_length=1, verbose_name='选项')),
            ],
            options={
                'verbose_name': '答题',
                'verbose_name_plural': '答题',
                'db_table': 'Xintest',
            },
        ),
        migrations.RemoveField(
            model_name='problem',
            name='is_reverse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AddField(
            model_name='test',
            name='tproblem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulate_test.problem', verbose_name='题目'),
        ),
        migrations.AddField(
            model_name='test',
            name='tuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulate_test.user', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='result',
            name='tuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulate_test.user', verbose_name='用户'),
        ),
    ]
