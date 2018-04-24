from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from .models import Comments
from .forms import CommentForms

def add_comment(request):
    context = {}
    form = CommentForms(request.POST, user=request.user)
    if request.is_ajax():
        print("Ajax请求")

    if form.is_valid():
        cmt_obj = Comments()
        cmt_obj.cmt_detail = form.cleaned_data['detail']
        cmt_obj.cmt_user = form.cleaned_data['user']
        cmt_obj.content_object = form.cleaned_data['content_object']

        reply_parent = form.cleaned_data['reply_parent']
        if not reply_parent is None:
            cmt_obj.reply_root = reply_parent.reply_root if not reply_parent.reply_root is None else reply_parent
            cmt_obj.reply_parent = reply_parent
            cmt_obj.reply_user = reply_parent.cmt_user

        cmt_obj.save()
        context['status'] = 'success'
        return JsonResponse(context)
    else:
        context['error_message'] = form.non_field_errors()
        print(form.errors)
    return JsonResponse(context)