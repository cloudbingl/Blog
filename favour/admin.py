from django.contrib import admin

from .models import FavourDetail,Favour
# Register your models here.

@admin.register(Favour)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'object_id', 'favour_num')


@admin.register(FavourDetail)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'object_id', 'user', 'date')
