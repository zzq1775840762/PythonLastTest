from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = '心理测试后台管理系统'
admin.site.site_title = '心理测试后台管理系统'
admin.site.index_title = '心理测试后台管理系统'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
#
#
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', ]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
   list_display = ['id','tuser','tproblem','option']
   list_filter = ['tuser','tproblem','option' ,]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'tuser', 'score', 'result',]
    list_filter = ['result', ]