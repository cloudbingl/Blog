from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from .models import Comments
from .forms import CommentForms

def add_comment(request):
    context = {}
    referer = request.META.get('HTTP_REFERER')
    print(referer)
    if request.method == "POST":
        form = CommentForms(request.POST)
        cnt_type = request.POST.get('model')
        obj_id = request.POST.get("model_id")
        ct = ContentType.objects.get(model=cnt_type)
        if form.is_valid():
            cmt_obj = Comments()
            cmt_obj.cmt_detail = form.cleaned_data['detail']
            cmt_obj.content_type = ct
            cmt_obj.object_id = int(obj_id)
            cmt_obj.cmt_user = request.user
            cmt_obj.save()
            messages.success(request, '评论成功')
        else:
            messages.warning(request, '评论失败')
        return redirect(referer)