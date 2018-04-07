from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ReadNum(models.Model):
    """阅读计数模型"""
    read_num = models.IntegerField(default=0, verbose_name='阅读量')
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING,
                                     verbose_name='对象模型')
    object_id = models.PositiveIntegerField(verbose_name="对象id")
    content_object = GenericForeignKey('content_type', 'object_id')



    class Meta:
        verbose_name = '阅读量'
        verbose_name_plural = verbose_name

