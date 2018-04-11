from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

from readstatistics.models import ReadDetail
from readstatistics.utils import ReadMethodMixin
from comment.utils import CommentMethodMixin


class Category(models.Model):
    """类目模型"""
    name = models.CharField(max_length=32, verbose_name="分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Articles(models.Model, ReadMethodMixin, CommentMethodMixin):
    """文章模型"""
    title = models.CharField(max_length=128, verbose_name="文章标题")
    detail = RichTextUploadingField(verbose_name="文章内容")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               verbose_name="作者")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    modify_date = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    pub_status = models.BooleanField(default=True, verbose_name="发布?")
    is_delete = models.BooleanField(default=False, verbose_name="删除?")
    cate = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                             verbose_name="分类")

    # GenericRelation() 不会影响表结构,只会作用于数据查询
    read_detail = GenericRelation(ReadDetail, related_query_name='articles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        # ordering = ('-pub_date',)
