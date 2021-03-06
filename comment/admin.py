from django.contrib import admin

from .models import Comments


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'object_id', 'cmt_user',  'reply_user', 'reply_parent_id', 'reply_root_id','cmt_date')

    # def save_model(self, request, obj, form, change):
    #     obj.cmt_user = request.user
    #     obj.save()