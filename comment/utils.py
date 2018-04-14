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
    def get_comments_data(self, reverse=False):
        ct = ContentType.objects.get_for_model(self)
        comments = Comments.objects.filter(content_type=ct, object_id=self.pk, reply_parent__isnull=True)
        if not reverse:
            comments = comments.order_by('-cmt_date')
        return comments


    def get_comment_form(self):
        kwargs = self.__init_comment_form()
        form = CommentForms(initial=kwargs)

        return form

    def __init_comment_form(self):
        ct = ContentType.objects.get_for_model(self)
        kwargs = {
            'content_type': ct.model,
            'object_id': self.pk,
            'reply_comment':0,
        }
        return kwargs

class CommentMethodMixin(CommentMethod, CommentNumMethod):
    pass
