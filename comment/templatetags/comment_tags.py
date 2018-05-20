from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comments


register = template.Library()

@register.simple_tag()
def get_comment_count(obj):
    ct = ContentType.objects.get_for_model(obj)
    return Comments.objects.filter(content_type=ct,object_id=obj.pk).count()