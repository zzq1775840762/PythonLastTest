from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    id = models.IntegerField(max_length=10, verbose_name='学号',primary_key=True)
    name = models.CharField(max_length=50, verbose_name='姓名', default='')
    gender = models.CharField(max_length=6, verbose_name='性别', choices=(('male', '男'), ('female', '女')), default='male')
    address = models.CharField(max_length=30, verbose_name='地址', default='')
    phone = models.CharField(max_length=11, verbose_name='电话', default='')

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        return self.id


class Problem(models.Model):
    id = models.AutoField(verbose_name='题号', primary_key=True)
    content = models.CharField(max_length=200, verbose_name='内容', default='')
    is_reverse = models.BooleanField(verbose_name='选项是否反向', default=False)

    class Meta:
        db_table = 'problem'
        verbose_name = '题目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.content:
            return self.content
        return self.id


class Record(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    times = models.IntegerField(max_length=10, verbose_name='测试次数')
    tuser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    tproblem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name='题目')
    option = models.CharField(max_length=1, verbose_name='选项')

    class Meta:
        db_table = 'record'
        verbose_name = '答题信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.option:
            return self.option
        return self.id