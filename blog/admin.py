from django.contrib import admin

from .models import Articles
from .models import Category


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'modify_date', 'is_delete')
    ordering = ['pub_date']
    search_fields = ['title']
    list_per_page = 10


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')