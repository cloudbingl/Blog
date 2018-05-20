from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class Favour(models.Model):
    # 记录文章点赞的数量
    favour_num = models.IntegerField(default=0, verbose_name='点赞量')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='模型')
    object_id = models.PositiveIntegerField(verbose_name='ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '点赞量'
        verbose_name_plural = verbose_name


class FavourDetail(models.Model):
    # 记录点赞的详细信息
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户名')
    date = models.DateTimeField(default=timezone.now, verbose_name='点赞时间')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='模型')
    object_id = models.PositiveIntegerField(verbose_name='ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '点赞详情'
        verbose_name_plural = verbose_name
