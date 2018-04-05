from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=128, verbose_name="文章标题")
    detail = RichTextUploadingField(verbose_name="文章内容")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               verbose_name="作者")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    modify_date = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    pub_status = models.BooleanField(default=True, verbose_name="发布状态")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        # ordering = ('-pub_date',)
