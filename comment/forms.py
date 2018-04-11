from django import forms
from ckeditor.widgets import CKEditorWidget
class CommentForms(forms.Form):
    detail = forms.CharField(
        widget=CKEditorWidget(
            config_name='ck_comment'),
        label='',
        error_messages={'required':'评论内容不能为空'})
