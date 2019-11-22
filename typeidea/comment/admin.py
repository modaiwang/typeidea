# Register your models here.
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommontAdmin(admin.ModelAdmin):
    list_display = (
        'target','nickname','content','website','created_time'
    )