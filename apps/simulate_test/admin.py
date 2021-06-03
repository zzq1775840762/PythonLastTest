from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = '心理测试后台管理系统'
admin.site.site_title = '心理测试后台管理系统'
admin.site.index_title = '心理测试后台管理系统'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'is_reverse',]


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass