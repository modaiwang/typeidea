# Register your models here.
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommontAdmin(admin.ModelAdmin):
    list_display = (
        'target','nickname','content','website','created_time'
    )
    fieldsets = (
        ('个人信息',{
            'description':'个人信息描述',
            'fields':(
                'nickname','email','website'
            )
        }),
        ('评论帖子',{
            'fields':(
                'target',
            )
        }),
        ('评论详情',{
            'fields':(
                'content',
            )
        }),

    )