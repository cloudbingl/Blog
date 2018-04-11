from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForms(forms.Form):
    detail = forms.CharField(required=True,
        widget=CKEditorWidget(
            config_name='ck_comment'),
    error_messages={'required': '评论内容不能为空'})

    def clean_detail(self):
        if not self.cleaned_data['detail']:
            raise forms.ValidationError('评论内容不能为空')