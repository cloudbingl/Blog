from django import forms
from django.contrib.contenttypes.models import ContentType
from ckeditor.widgets import CKEditorWidget

from .models import Comments


class CommentForms(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    detail = forms.CharField(widget=CKEditorWidget(config_name='ck_comment'))

    reply_comment = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForms, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')

        ct = self.cleaned_data['content_type']
        obj_id = self.cleaned_data['object_id']

        try:
            model_class = ContentType.objects.get(model=ct).model_class()
            model_obj = model_class.objects.get(pk=obj_id)
            self.cleaned_data['content_object'] = model_obj
        except:
            raise forms.ValidationError('评论的对象不存在')

        return self.cleaned_data

    def clean_reply_comment(self):
        reply_comment_id = self.cleaned_data['reply_comment']
        if reply_comment_id < 0:
            forms.ValidationError('回复发生了异常！')
        elif reply_comment_id == 0:
            self.cleaned_data['reply_parent'] = None
        elif Comments.objects.filter(pk=reply_comment_id).exists():
            self.cleaned_data['reply_parent'] = Comments.objects.get(pk=reply_comment_id)
        else:
            forms.ValidationError('回复发生了异常！')
        return reply_comment_id