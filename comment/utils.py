from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .models import Comments
from .forms import CommentForms


class CommentNumMethod(object):
    def get_comment_num(self):
        ct = ContentType.objects.get_for_model(self)
        comment_num = Comments.objects.filter(content_type=ct,
                                              object_id=self.pk).count()
        return comment_num


class CommentMethod(object):
    def get_comments_data(self):
        ct = ContentType.objects.get_for_model(self)
        comments = Comments.objects.filter(content_type=ct, object_id=self.pk)
        return comments

    @staticmethod
    def get_comment_form():
        form = CommentForms()
        return form

class CommentMethodMixin(CommentMethod, CommentNumMethod):
    pass
