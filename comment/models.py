from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comments(models.Model):
    """评论"""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     verbose_name='评论对象')
    object_id = models.PositiveIntegerField(verbose_name='对象id')
    content_object = GenericForeignKey('content_type', 'object_id')

    cmt_detail = models.TextField(verbose_name='评论内容')
    cmt_user = models.ForeignKey(User, related_name='cmt_user', on_delete=models.CASCADE, verbose_name='评论用户')
    cmt_date = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    cmt_is_delete = models.BooleanField(default=False, verbose_name='删除?')

    # reply_root：回复评论 -> 根节点(回复评论的第一条)
    # reply_parent：回复 -> 评论
    # reply_user：回复 -> 谁
    # 三个字段都为 null 时，是对文章直接评论的
    reply_root = models.ForeignKey('self', null=True, blank=True , related_name='rpy_root', on_delete=models.CASCADE, verbose_name='评论根节点')
    reply_parent = models.ForeignKey('self', null=True, blank=True, related_name='rpy_parent', on_delete=models.CASCADE, verbose_name='评论父节点')
    reply_user = models.ForeignKey(User, null=True, related_name='rpy_user', on_delete=models.CASCADE, verbose_name='回复用户')

    def __str__(self):
        return self.cmt_detail

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name




