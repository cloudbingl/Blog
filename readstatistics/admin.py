from django.contrib import admin

from .models import ReadDetail
from .models import ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'date_read_num', 'content_object')
