from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from .models import Comments
from .forms import CommentForms

def add_comment(request):
    context = {}
    form = CommentForms(request.POST, user=request.user)
    if form.is_valid():
        cmt_obj = Comments()
        cmt_obj.cmt_detail = form.cleaned_data['detail']
        cmt_obj.cmt_user = form.cleaned_data['user']
        cmt_obj.content_object = form.cleaned_data['content_object']
        cmt_obj.save()
        context['status'] = 'success'
        return JsonResponse(context)
    else:
        context['error_message'] = form.non_field_errors()
        print(form.errors)
    return JsonResponse(context)