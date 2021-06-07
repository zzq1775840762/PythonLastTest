from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=10,verbose_name='学号',primary_key=True)
    name = models.CharField(max_length=50, verbose_name='姓名', default='')

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        return self.id


class Problem(models.Model):
    id = models.AutoField(verbose_name='题号', primary_key=True)
    content = models.CharField(max_length=200, verbose_name='内容', default='')

    class Meta:
        db_table = 'problem'
        verbose_name = '题目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.content:
            return self.content
        return self.id


class Test(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    tuser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    tproblem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name='题目')
    option = models.IntegerField(verbose_name='选项')

    class Meta:
        db_table = 'Xintest'
        verbose_name = '答题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.tuser.name)


class Result(models.Model):
    tuser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    score = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='得分')
    result = models.IntegerField(verbose_name='类别')

    class Meta:
        db_table = 'Result'
        verbose_name = '答题结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.result:
            return self.result
        return self.tuser
