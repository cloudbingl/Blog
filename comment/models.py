from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comments(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING,
                                     verbose_name='评论对象')
    object_id = models.PositiveIntegerField(verbose_name='对象id')
    content_object = GenericForeignKey('content_type', 'object_id')

    cmt_detail = models.TextField(verbose_name='评论内容')
    cmt_user = models.ForeignKey(User ,on_delete=models.DO_NOTHING ,verbose_name='评论用户')
    cmt_date = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    cmt_is_delete = models.BooleanField(default=False, verbose_name='删除?')

    def __str__(self):
        return self.cmt_detail

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name




